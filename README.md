Simple-events
---
#### Description
Simple events api  built with postgres, python, flask and graphene libarary for graphql.

##### Development
---
We assume that:
```
- Python 3 is installed.
- Postgres is installed.
- virtualenv packaged is installed.
```

In order to run the api locally kindly refer to the section below we have the following as:
- Clone the repo.
    ```
    git clone https://github.com/owenbob/simple-events.git
    ```
- Create two  databases `dev` and `test`.  Identify their database uris.
- Create virtual enviroment and activate it. For example
    ```
    virtualenv --python=python3 venv
    
    source venv/bin/activate
    ```
- Export environment variables. Refer below for an example:
    ```
    # dev db
    export EVENTS_DEV_DATABASE_URI="Your development uri"
    
    # app secret
    export EVENTS_APP_SECRET="Your app secret."
    
    # target event
    # This is for when your wnat to generate multiple services.
    export TARGET_SERVICE="Your target service, default is events."
    
    # target environment
    # your can create various environment for which you want to run your application. the defaults are dev, test and  prod.
    export ENV="Environment you want to work with, default is dev"
    ```
- Install dependencies.
    ```
    pip install -r requirements.txt
    ```
- Run migration. The application utilises alembic package to run its migration.
    ```
    alembic revision --autogenerate -m "migration message"
    
    alembic upgrade head
    ```
    
- Run application. 
    ```
    python runner.py
    ```

- Once the server is running , open a browser tab and input the home endpoint to access the graphql query interface.
Refer to the documentation explorer to see what `queries` and `mutations` are available.
    ```
    http://localhost:5000/graphql
    ```
#### Testing
---
##### Unit Testing
Running Unit tests to test key functionality.

- export testing environment variables. refer to example below:

    ```
    # app secret
    export EVENTS_APP_SECRET="Your app secret."
    
    # test db
    export EVENTS_TEST_DATABASE_URI="Your test database uri"
    
    # test environment
    export ENV="test"
    ```
- Run tests.
    ```
    pytest tests/ -vv
    ```
##### Load Testing
It is important to carry out load testing to determine and ensure the api has maximum reliablity at all times. A highly recommended library to achieve this is 
[locust](https://locust.io/) and that is what I would use to test api behaviour under different stress enviroments.

##### Security Testing
Security in todays world is very key. Backend services should have a security criteria that they subscribe to. Such guidelines would include procedures like:
```
- No leakage of secrets so carrying out security audits to ensure secret key managers are utilised.
- Ensuring that Authentication mechanisms are set up to ensure users are who they are.
- Authorization policies are well defined to ensure that users access what they are supposed to. You can use a third party auth manager like okta to ensure these policies are strictly adhered to.
-  Ensuring correct data encryption and managing all decryption points.
```
#### Growing Business logic
With the right configuration settings we can grow the capability what a service can handle for example. This example has mainly catered for an events service but we can add more components to this service. For example by creating a `service.py`.
```
"""
By using the AllQueries and AllMutations classes we are
able to add other query and mutation classes.

This enables us to create other modules/components/apps with their own
queries and mutation and then combine them to create one schema
for the service for example we can create a payments module/component/app:
"""
from common.app_creation import create_app
from config.config import application_configuration
from payment.schema import PaymentsQuery, PaymentMutation
from delivery.schema import DeliveryQuery, DeliveryMutation 
from events.schema import EventsQuery, EventsMutation

class AllQueries(EventsQuery, PaymentsQuery, DeliveryQuery):
    pass


class AllMutations(EventsMutation, PaymentMutation, DeliveryMutation):
    pass
    
    
service_schema = Schema(query=AllQueries, mutation=AllMutations)

service_config = application_configuration
service_app = create_app(
    schema=service_schema,
    config=service_config
)

```
Creating and publishing custom or organisation business logic packages for example  an analytics package that houses key methods and classes for calculating common business operations that are shared across various stages of business could be a way to host common dependecies for example business.analytics, business.taxes package
```
pip install business.analtyics --extra-index-url https://custom-business-package-repository
```
```
from business.taxes import VAT_RATE, calculate_all_tax, COVID_TAX_RELIEF

all_items = get_all_items()
all_tax_to pay = calculate_tax(all_items) * COVID_TAX_RELIEF
```

Several application instances can be created this way  and each can have its own runner for example:
```
"""
Run  application instance or instances.
"""

from service import service_app

PORT = "Port to run on"
if __name__ == '__main__':
    service_app.run(port=PORT)

```

#### Scaling  the Application
---

Handling Multiple requests.
- It is imperative that requests are handled in and efficient and scalable. In order to ensure efficiency and fast reply we need to set up a mechanism to make sure request processing resources are available to process requests and not pro-occupied. Using `graphql` we can ensure that requests are efficent in the way that their generating by requesting for only that data that we need, preventing overfetching and underfetching hence cutting down the size of request responses and the number of requests made. Batching queries enable single requests to be made to the service.
- The other resource intensive activity is searching the data store for certain values. Utilising elastic search we can be able to get the benefits of fast search engine.
You can utilise the [graphene-elastic](https://graphene-elastic.readthedocs.io/en/latest/)  package to rip these benefits.
- Implementing an in-memory data store  like [Redis](https://redis-py.readthedocs.io/en/stable/) to provide caching would greatly the speed at which requests are processed through fast read and write operations and.
- Database Pooling is another way to greatly scale since database connections for requests are one of the most resource intensive operations.
- Utilising Inflastructure as a service set up we are able to ensure various scalability possibilities like at various stages of the application for example load balancing to redirect traffic to more healthier instances.

- In order to achieve a stable, agile ande contionously growing application I would apply the [Twelve Factor app](https://12factor.net/) methodology.
