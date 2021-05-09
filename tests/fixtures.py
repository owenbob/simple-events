

seed_test_events_query = r"""
    mutation{
    firstQuery: saveEvent(
        email: "johndoe@johndoe.com",
        component: "orders",
        environment: "production",
        message:"the buyer 123456 has placed an order successfully",
        data: "{\"order_id\": 123, \"amount\": 300, \"created_at\": 1526123095}"
    ){
        event{
        id
        createdAt
        email
        environment
        component
        message
        data
        }
    }
    secondQuery: saveEvent(
        email: "johndoe@johndoe.com",
        component: "orders",
        environment: "production",
        message:"the buyer 456 has placed an order successfully",
        data: "{\"order_id\": 456, \"amount\": 400, \"created_at\": 1526123097}"
    ){
        event{
        id
        createdAt
        email
        environment
        component
        message
        data
        }
    }
    thirdQuery: saveEvent(
        email: "johndoe@johndoe.com",
        component: "inventory",
        environment: "production",
        message:"error in inventory update",
        data: "{\"error\": 56, \"service\": 500, \"created_at\": 1526123097}"
    ){
        event{
        id
        createdAt
        email
        environment
        component
        message
        data
        }
    }
    }

"""


save_event_query = r"""
    mutation{
        saveEvent(
            email: "johndoe@johndoe.com",
            component: "orders",
            environment: "production",
            message:"the buyer 123456 has placed an order successfully",
            data: "{\"order_id\": 123, \"amount\": 300, \"created_at\": 1526123095}"
        ){
            event{email
            environment
            component
            message
            }
        }
    }
"""


expected_save_event_result = {
  "data": {
    "saveEvent": {
      "event": {
        "email": "johndoe@johndoe.com",
        "environment": "production",
        "component": "orders",
        "message": "the buyer 123456 has placed an order successfully"
      }
    }
  }
}


all_events = """
    query{
        events{
            id
            email
            component
            message
            createdAt
            message
            data
        }
    }
"""


query_by_paramaters_with_all_matching = """
    query{
    eventsByParameters(
        email:"johndoe@johndoe.com",
        environment: "production",
        component:"inventory",
        text:"error",
        date: "1-1-2018"
    ){
        email
        component
        message
    }
    }
"""


expected_query_by_paramaters_with_match = {
  "data": {
    "eventsByParameters": [
      {
        "email": "johndoe@johndoe.com",
        "component": "inventory",
        "message": "error in inventory update"
      }
    ]
  }
}


query_by_paramaters_with_no_match = """
    query{
    eventsByParameters(
        email:"johndoe@johndoe.com",
        environment: "production",
        component:"inventory",
        text:"success",
        date: "1-1-2018"
    ){
        email
        component
        message
    }
    }
"""

expected_query_by_paramaters_with_no_match = {
  "data": {
    "eventsByParameters": []
  }
}
