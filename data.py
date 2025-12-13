class Person:
       
       grey = {"firstName" : "Игорь",
        "lastName" : "Игорь",
        "address" : "Москва",
        "metroStation" : "ЦСКА",
        "phone" : "89008889999",
        "rentTime" : 2,
        "deliveryDate" : "2025-12-24",
        "comment" : "21",
        "color" : ["GREY"]}
       black = {"firstName" : "Игорь",
        "lastName" : "Игорь",
        "address" : "Москва",
        "metroStation" : "ЦСКА",
        "phone" : "89008889999",
        "rentTime" : 2,
        "deliveryDate" : "2025-12-24",
        "comment" : "21",
        "color" : ["BLACK"]}
       
       withoutColor = {"firstName" : "Игорь",
        "lastName" : "Игорь",
        "address" : "Москва",
        "metroStation" : "ЗИЛ",
        "phone" : "89008889999",
        "rentTime" : 2,
        "deliveryDate" : "05.12.2025",
        "comment" : "21"}
       
       withColor = {"firstName" : "Игорь",
        "lastName" : "Игорь",
        "address" : "Москва",
        "metroStation" : "ЗИЛ",
        "phone" : "89008889999",
        "rentTime" : 2,
        "deliveryDate" : "05.12.2025",
        "comment" : "21",
        "color" : ["BLACK", "GREY"]}
       
       lst1 = [withColor, black, grey, withoutColor]

       courier_without_login = {
              "password": "1234",
              "firstName": "saske"
              }
       courier_without_password = {
              "login": "ninja",
              "firstName": "saske"
              }
       
       invalid_courier = [courier_without_password, courier_without_login]

       invalid_login = [("", "ninja"), ("1234", "")]
       track_none = ""
       track_invalid = "13527899"
       invalid_accept = [("", "2345"), ("1234", "")]