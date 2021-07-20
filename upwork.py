# from flask import Flask
#
# app1 = Flask(__name__)
#
# @app1.route('/upwork', methods=["GET"])
# def upwork():
#     return {
#         "status": True,
#         "services": [
#             {
#                 "serviceId": "5f980ce1cd54221204831b93",
#                 "serviceName": "Car Service",
#                 "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Basic+Service.jpg",
#                 "subServices": [
#                     {
#                         "addedToCart": True,
#                         "price": "2399",
#                         "subServiceId": "5f99612164d15e001edd7bed",
#                         "subServiceName": "Basic Service",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/ENgine+%26+Basic+Service.jpg",
#                         "description": "Prevention is always better than cure. And that, wholly explains AutoFlipz Basic Service. This service aims at the prevention of car breakdowns and failures. Regular vehicle maintenance helps optimize the performance, reliability, safety and durability of the car, while ensuring a good resale value.  Basic car servicing is essential for a smooth and trouble-free car ownership experience.",
#                         "brief": "Takes 2 hours /nWarranty 2 Months /nEvery 5000 Kms / 3 months",
#                         "serviceId": "5f980ce1cd54221204831b93",
#                         "serviceName": "Car Service",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Basic+Service.jpg",
#                         "defaultAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fc380927f79362b9c7425b4",
#                                 "name": "Engine Oil"
#                             }
#                         ],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a4e6ce84d6001eaee533",
#                                 "name": "AC Filter"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa6764d15e001edd7c2c",
#                                 "name": "Throttle Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99913964d15e001edd7c04",
#                                 "name": "Rubbing/Polishing"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Service.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5f9a672764d15e001edd7c2f",
#                                 "name": "Engine Oil"
#                             },
#                             {
#                                 "_id": "5f9a679f64d15e001edd7c30",
#                                 "name": "Oil Filter "
#                             },
#                             {
#                                 "_id": "5f9a67d764d15e001edd7c31",
#                                 "name": "Air Filter"
#                             },
#                             {
#                                 "_id": "5f9a67f264d15e001edd7c32",
#                                 "name": "Coolant"
#                             },
#                             {
#                                 "_id": "5f9a681b64d15e001edd7c34",
#                                 "name": "Battery Water "
#                             },
#                             {
#                                 "_id": "5f9a680864d15e001edd7c33",
#                                 "name": "Wiper Fluid "
#                             },
#                             {
#                                 "_id": "5f9a683564d15e001edd7c35",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "_id": "5f9a6a1e64d15e001edd7c37",
#                                 "name": "Interior"
#                             },
#                             {
#                                 "_id": "5f9a6a0164d15e001edd7c36",
#                                 "name": "Exterior Body"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2779",
#                         "subServiceId": "5f9961b564d15e001edd7bee",
#                         "subServiceName": "Standard Service",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Standard+Service.jpg",
#                         "description": "A well-cared car will run and look better in the long run and always hold a higher value.  The most popular service package to utilize your vehicle to its maximum potential. If inspection and maintenance is avoided, it may have drastic results with respect to sudden cost incurring damages. Engine Oil & filter are needed to extend engine life, maintain lubricants, cool the components, improve mileage and it adds to overall longevity of the vehicle. Save money on repairs in future and opt for AutoFlipz Standard Service Package.",
#                         "brief": "Basic service with some additional services.",
#                         "serviceId": "5f980ce1cd54221204831b93",
#                         "serviceName": "Car Service",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Basic+Service.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99913964d15e001edd7c04",
#                                 "name": "Rubbing/Polishing"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a4e6ce84d6001eaee533",
#                                 "name": "AC Filter"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a506ce84d6001eaee534",
#                                 "name": "Radiator Flushing"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Service.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5f9a672764d15e001edd7c2f",
#                                 "name": "Engine Oil"
#                             },
#                             {
#                                 "_id": "5f9a6bab64d15e001edd7c38",
#                                 "name": "Air Filter"
#                             },
#                             {
#                                 "_id": "5f9a679f64d15e001edd7c30",
#                                 "name": "Oil Filter "
#                             },
#                             {
#                                 "_id": "5f9a67f264d15e001edd7c32",
#                                 "name": "Coolant"
#                             },
#                             {
#                                 "_id": "5f9a681b64d15e001edd7c34",
#                                 "name": "Battery Water "
#                             },
#                             {
#                                 "_id": "5f9a6c2b64d15e001edd7c3b",
#                                 "name": "Brake Fluid"
#                             },
#                             {
#                                 "_id": "5f9a6bfe64d15e001edd7c3a",
#                                 "name": "Cabin Filter / AC Filter "
#                             },
#                             {
#                                 "_id": "5f9a6cd464d15e001edd7c3d",
#                                 "name": "Front Brake Pads"
#                             },
#                             {
#                                 "_id": "5f9a6cb364d15e001edd7c3c",
#                                 "name": "Rear Brake Shoes"
#                             },
#                             {
#                                 "_id": "5f9a6bc964d15e001edd7c39",
#                                 "name": "Fuel Filter"
#                             },
#                             {
#                                 "_id": "5f9a683564d15e001edd7c35",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "_id": "5f9a6ee164d15e001edd7c3e",
#                                 "name": "Car"
#                             },
#                             {
#                                 "_id": "5f9a6a0164d15e001edd7c36",
#                                 "name": "Exterior Body"
#                             },
#                             {
#                                 "_id": "5f9a6a1e64d15e001edd7c37",
#                                 "name": "Interior"
#                             },
#                             {
#                                 "_id": "5f9a680864d15e001edd7c33",
#                                 "name": "Wiper Fluid "
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "3499",
#                         "subServiceId": "5f99633764d15e001edd7bef",
#                         "subServiceName": "Comprehensive Service",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/DSC_0275.png",
#                         "description": "Looking to keep your car functioning smoothly? AutoFlipz provide a comprehensive range of services to keep your car running smoothly. With our team of experienced mechanics and state of the art tools & techniques, We would always keep your car in top condition. Our service includes a 50 point check-up along with the Replacements of consumables & spare parts With top ups of fluids (coolant, gear oil, wiper fluid). Through regular vehicle inspections and maintenance, the overall performance of the vehicle can be optimized. In addition, it helps avoid more expensive repairs that one may need to incur in the near future. Now is the time to begin to think smarter & opt for AutoFlipz's Signature Package. ",
#                         "brief": "Autoflipz's Signature Car Service Package. ",
#                         "serviceId": "5f980ce1cd54221204831b93",
#                         "serviceName": "Car Service",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Basic+Service.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa2864d15e001edd7c2b",
#                                 "name": "Injector Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a4e6ce84d6001eaee533",
#                                 "name": "AC Filter"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99913964d15e001edd7c04",
#                                 "name": "Rubbing/Polishing"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Service.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Wheel+Alignment.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5f9a672764d15e001edd7c2f",
#                                 "name": "Engine Oil"
#                             },
#                             {
#                                 "_id": "5f9a6bab64d15e001edd7c38",
#                                 "name": "Air Filter"
#                             },
#                             {
#                                 "_id": "5f9a679f64d15e001edd7c30",
#                                 "name": "Oil Filter "
#                             },
#                             {
#                                 "_id": "5f9a6bfe64d15e001edd7c3a",
#                                 "name": "Cabin Filter / AC Filter "
#                             },
#                             {
#                                 "_id": "5f9a6bc964d15e001edd7c39",
#                                 "name": "Fuel Filter"
#                             },
#                             {
#                                 "_id": "5f9a680864d15e001edd7c33",
#                                 "name": "Wiper Fluid "
#                             },
#                             {
#                                 "_id": "5f9a67f264d15e001edd7c32",
#                                 "name": "Coolant"
#                             },
#                             {
#                                 "_id": "5f9a681b64d15e001edd7c34",
#                                 "name": "Battery Water "
#                             },
#                             {
#                                 "_id": "5f9a6c2b64d15e001edd7c3b",
#                                 "name": "Brake Fluid"
#                             },
#                             {
#                                 "_id": "5f9a6cd464d15e001edd7c3d",
#                                 "name": "Front Brake Pads"
#                             },
#                             {
#                                 "_id": "5f9a6cb364d15e001edd7c3c",
#                                 "name": "Rear Brake Shoes"
#                             },
#                             {
#                                 "_id": "5f9a6a0164d15e001edd7c36",
#                                 "name": "Exterior Body"
#                             },
#                             {
#                                 "_id": "5f9a6a1e64d15e001edd7c37",
#                                 "name": "Interior"
#                             },
#                             {
#                                 "_id": "5f9a683564d15e001edd7c35",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "_id": "5f9a740264d15e001edd7c3f",
#                                 "name": "Wheel"
#                             },
#                             {
#                                 "_id": "5f9a741064d15e001edd7c40",
#                                 "name": "Wheel"
#                             },
#                             {
#                                 "_id": "5f9a742464d15e001edd7c41",
#                                 "name": "Wheel"
#                             },
#                             {
#                                 "_id": "5f9a744c64d15e001edd7c43",
#                                 "name": "Throttle Body"
#                             },
#                             {
#                                 "_id": "5f9a6ee164d15e001edd7c3e",
#                                 "name": "Car"
#                             },
#                             {
#                                 "_id": "5f9a743664d15e001edd7c42",
#                                 "name": "Gear Oil"
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "serviceId": "5f980d01cd54221204831b94",
#                 "serviceName": "Car Care",
#                 "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Car+CAre+Head.png",
#                 "subServices": [
#                     {
#                         "addedToCart": False,
#                         "price": "499",
#                         "subServiceId": "5f99907f64d15e001edd7c02",
#                         "subServiceName": "Car Wash",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Car+Wash.png",
#                         "description": "Having a shiny car is something that many people wish to achieve, as it can show off a nice car and make you look good.  Your car's exterior has plenty of enemies from the harsh sun to rain, snow, salt and even bird droppings. Regular Car Wash removes all the dirt, mud, dust and bring back the new car feeling. At AutoFlipz, Don't just wash your car, Super Shine it !",
#                         "brief": "Remove dust & mud & maintains everyday shine.",
#                         "serviceId": "5f980d01cd54221204831b94",
#                         "serviceName": "Car Care",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Car+CAre+Head.png",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e78e4b6940001e8c703b",
#                                 "name": "Interior Steam Wash"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99913964d15e001edd7c04",
#                                 "name": "Rubbing/Polishing"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fb75f93b66787001e93b331",
#                                 "name": "Exterior Body"
#                             },
#                             {
#                                 "_id": "5fb75fb7b66787001e93b332",
#                                 "name": "Seats & Boot"
#                             },
#                             {
#                                 "_id": "5fb75fdbb66787001e93b333",
#                                 "name": "Foot Mats"
#                             },
#                             {
#                                 "_id": "5fb7610eb66787001e93b335",
#                                 "name": "Underbody"
#                             },
#                             {
#                                 "_id": "5fb7612db66787001e93b336",
#                                 "name": "Gate Frames"
#                             },
#                             {
#                                 "_id": "5f9a6a0164d15e001edd7c36",
#                                 "name": "Exterior Body"
#                             },
#                             {
#                                 "_id": "5fb76157b66787001e93b338",
#                                 "name": "Interior"
#                             },
#                             {
#                                 "_id": "5fb7616bb66787001e93b339",
#                                 "name": "AC Vents"
#                             },
#                             {
#                                 "_id": "5fb7618ab66787001e93b33a",
#                                 "name": "Engine"
#                             },
#                             {
#                                 "_id": "5fb76141b66787001e93b337",
#                                 "name": "Dashboard"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "1599",
#                         "subServiceId": "5f9990df64d15e001edd7c03",
#                         "subServiceName": "Complete Car Detailing",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Complete+car.png",
#                         "description": "“I want the inside and the outside cleaned…ALL of it!”  Whether a car interior is infected with the day to day kid’s messness, or the vehicle’s exterior is tarnished with light swirl marks.  Simply put, getting your car detailed means a top-to-bottom thorough cleaning of your car using specialized tools and products.  At AutoFlipz, Car detailing involves cleaning and reconditioning the interior and exterior of the car. The aim of this is to restore the paintwork by eliminating scratches or swirl marks to make the car look almost brand new like it did when you first drove it out of the showroom.",
#                         "brief": "Make your car shine like brand new.",
#                         "serviceId": "5f980d01cd54221204831b94",
#                         "serviceName": "Car Care",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Car+CAre+Head.png",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa2864d15e001edd7c2b",
#                                 "name": "Injector Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa6764d15e001edd7c2c",
#                                 "name": "Throttle Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a506ce84d6001eaee534",
#                                 "name": "Radiator Flushing"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fb785ebb66787001e93b33c",
#                                 "name": "Interior"
#                             },
#                             {
#                                 "_id": "5fb78609b66787001e93b33d",
#                                 "name": "Interior"
#                             },
#                             {
#                                 "_id": "5fb78629b66787001e93b33e",
#                                 "name": "AC Vent"
#                             },
#                             {
#                                 "_id": "5fb78646b66787001e93b33f",
#                                 "name": "Dashboard"
#                             },
#                             {
#                                 "_id": "5fb7865ab66787001e93b340",
#                                 "name": "Door Pads"
#                             },
#                             {
#                                 "_id": "5fb78677b66787001e93b341",
#                                 "name": "Vinyl & Rubber Parts"
#                             },
#                             {
#                                 "_id": "5fb78689b66787001e93b342",
#                                 "name": "Seats"
#                             },
#                             {
#                                 "_id": "5fb7869cb66787001e93b343",
#                                 "name": "Roof Lining"
#                             },
#                             {
#                                 "_id": "5fb786b0b66787001e93b344",
#                                 "name": "Carpet"
#                             },
#                             {
#                                 "_id": "5fb786c2b66787001e93b345",
#                                 "name": "Boot"
#                             },
#                             {
#                                 "_id": "5fb786d2b66787001e93b346",
#                                 "name": "Glass"
#                             },
#                             {
#                                 "_id": "5fb75ff0b66787001e93b334",
#                                 "name": "Exterior Body"
#                             },
#                             {
#                                 "_id": "5fb7618ab66787001e93b33a",
#                                 "name": "Engine"
#                             },
#                             {
#                                 "_id": "5fb7872fb66787001e93b34a",
#                                 "name": "Exterior "
#                             },
#                             {
#                                 "_id": "5fb7870fb66787001e93b348",
#                                 "name": "Scratch"
#                             },
#                             {
#                                 "_id": "5fb78743b66787001e93b34b",
#                                 "name": "Tyre"
#                             },
#                             {
#                                 "_id": "5fb78766b66787001e93b34d",
#                                 "name": "Interior"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "949",
#                         "subServiceId": "5f99913964d15e001edd7c04",
#                         "subServiceName": "Rubbing/Polishing",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/R%26P.jpg",
#                         "description": "No matter how well you take care of your car, its exterior will begin to lose its overall exterior appearance over time. Exterior Rubbing and Polishing your car will help to extend the life and beauty of the paint and exterior.  Hence to keep your car’s exterior in good shape, you would want to get it done by AutoFlipz at regular intervals. Dirt, dust, tree sap, bird droppings, and other contaminants are removed from the car’s exterior so that they cannot cause further damage to the paint coatings.",
#                         "brief": "Removes scratches & stains from your car body.",
#                         "serviceId": "5f980d01cd54221204831b94",
#                         "serviceName": "Car Care",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Car+CAre+Head.png",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fcf28bf561f56001e20e9e9",
#                                 "name": "Interior Vacuuming"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fb78b73b66787001e93b34e",
#                                 "name": "Exterior Body"
#                             },
#                             {
#                                 "_id": "5fb78b83b66787001e93b34f",
#                                 "name": "Exterior Body"
#                             },
#                             {
#                                 "_id": "5fb78b91b66787001e93b350",
#                                 "name": "Wax"
#                             },
#                             {
#                                 "_id": "5fb78b9fb66787001e93b351",
#                                 "name": "Exterior "
#                             },
#                             {
#                                 "_id": "5fb78badb66787001e93b352",
#                                 "name": "Interior"
#                             },
#                             {
#                                 "_id": "5fb78be5b66787001e93b353",
#                                 "name": "Windshield "
#                             },
#                             {
#                                 "_id": "5fb7870fb66787001e93b348",
#                                 "name": "Scratch"
#                             },
#                             {
#                                 "_id": "5fb78743b66787001e93b34b",
#                                 "name": "Tyre"
#                             },
#                             {
#                                 "_id": "5fb786d2b66787001e93b346",
#                                 "name": "Glass"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "899",
#                         "subServiceId": "5f99933464d15e001edd7c06",
#                         "subServiceName": "Interior Dry Cleaning",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Dry+Cleaning.jpg",
#                         "description": "For most car owners, the priority is always to keep the outside of the car clear. This makes sense as that’s what the others see. When you overlook the cleanliness of the interior of your car, your car’s interior surfaces could start to develop faster wear and tear. Just as important as keeping your car exterior clean, having a clean interior is an essential part of preventive maintenance. Regular Interior cleaning removes all the dirt, mud, dust and bring back the new car feeling. With professional Car Interior Cleaning at AutoFlipz, you will be able to restore your car so that it feels and smells brand new when you’re in.",
#                         "brief": "Keep your car interior clear & shining.",
#                         "serviceId": "5f980d01cd54221204831b94",
#                         "serviceName": "Car Care",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Car+CAre+Head.png",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99a7aa64d15e001edd7c20",
#                                 "name": "Teflon Coating"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7444b6940001e8c703a",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fb78689b66787001e93b342",
#                                 "name": "Seats"
#                             },
#                             {
#                                 "_id": "5fb786b0b66787001e93b344",
#                                 "name": "Carpet"
#                             },
#                             {
#                                 "_id": "5fb786d2b66787001e93b346",
#                                 "name": "Glass"
#                             },
#                             {
#                                 "_id": "5fba210e81eb8d001e7e7f87",
#                                 "name": "Windshield "
#                             },
#                             {
#                                 "_id": "5fba213181eb8d001e7e7f88",
#                                 "name": "AC Vents & Grill"
#                             },
#                             {
#                                 "_id": "5fba214081eb8d001e7e7f89",
#                                 "name": "Roof"
#                             },
#                             {
#                                 "_id": "5fba215981eb8d001e7e7f8b",
#                                 "name": "Interior"
#                             },
#                             {
#                                 "_id": "5fba217681eb8d001e7e7f8c",
#                                 "name": "Indoor Gates"
#                             },
#                             {
#                                 "_id": "5fba215081eb8d001e7e7f8a",
#                                 "name": "Dashboard"
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "serviceId": "5f980e1a99fd6b127b820cae",
#                 "serviceName": "Inspection",
#                 "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                 "subServices": [
#                     {
#                         "addedToCart": False,
#                         "price": "799",
#                         "subServiceId": "5f9992e864d15e001edd7c05",
#                         "subServiceName": "Pre Purchase Inspection",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Standard+Service.jpg",
#                         "description": "Whether you’re looking to buy your next car or are hoping to give a potential buyer more confidence in your car’s reliability – we have you covered. AutoFlipz offers greater confidence and peace of mind to car buyers and sellers by providing comprehensive pre-purchase car inspections, roadworthy inspection service, and vehicle health checks.  With AutoFlipz at your side, you'll never have to wonder whether the used car you're buying is in the condition the seller claims. We'll reveal every detail - from the condition of its mechanical and electrical parts to its accident history. Feel safe and secure in your car purchase with AutoFlipz !!",
#                         "brief": "Fastest and easiest way to make a confident car purchase or sale.",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7444b6940001e8c703a",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Pre+Purchase+1.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/PRE+PURCHASE+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fb78dedb66787001e93b355",
#                                 "name": "Engine "
#                             },
#                             {
#                                 "_id": "5fb78dfcb66787001e93b356",
#                                 "name": "Battery"
#                             },
#                             {
#                                 "_id": "5fb78e0fb66787001e93b357",
#                                 "name": "Axles and Exhaust"
#                             },
#                             {
#                                 "_id": "5fb78e3cb66787001e93b358",
#                                 "name": "Clutch"
#                             },
#                             {
#                                 "_id": "5fb78e4eb66787001e93b359",
#                                 "name": "Wheel Assembly"
#                             },
#                             {
#                                 "_id": "5fb78e5cb66787001e93b35a",
#                                 "name": "Dashboard"
#                             },
#                             {
#                                 "_id": "5fb78e6bb66787001e93b35b",
#                                 "name": "Fluids"
#                             },
#                             {
#                                 "_id": "5fb78e7ab66787001e93b35c",
#                                 "name": "Suspension"
#                             },
#                             {
#                                 "_id": "5fb78e88b66787001e93b35d",
#                                 "name": "Electricals"
#                             },
#                             {
#                                 "_id": "5fb78ea3b66787001e93b35f",
#                                 "name": "Brakes"
#                             },
#                             {
#                                 "_id": "5fb78eb2b66787001e93b360",
#                                 "name": "AC"
#                             },
#                             {
#                                 "_id": "5fb78ec1b66787001e93b361",
#                                 "name": "Body Panel"
#                             },
#                             {
#                                 "_id": "5fb78ed3b66787001e93b362",
#                                 "name": "Transmission"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5fc3513dce84d6001eaee521",
#                         "subServiceName": "Brakes",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Brakes.jpg",
#                         "description": "The AutoFlipz's technical experts and trained staff will investigate your car and conduct a thorough evaluation. Following this, the malfunctioning brake components will be replaced.",
#                         "brief": "Is your steering wheel feeling shaky?",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fcf28bf561f56001e20e9e9",
#                                 "name": "Interior Vacuuming"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99913964d15e001edd7c04",
#                                 "name": "Rubbing/Polishing"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Brakes+1.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Brakes+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fcc94f4561f56001e20e9ae",
#                                 "name": "Front Brake"
#                             },
#                             {
#                                 "_id": "5fcc94fe561f56001e20e9af",
#                                 "name": "Rear Brake "
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5fc35193ce84d6001eaee522",
#                         "subServiceName": "Clutch",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Clutch.png",
#                         "description": "Is there a burning paper smell in your car? Is your transmission slipping gears? Or is your clutch sticking?  Such situations may arise when the clutch is worn out and in need of repair or replacement, depending on the severity. Have it inspected by a AutoFlipz's expert to save you from the dangers that a clutch-fail might cause.",
#                         "brief": "Get your car's clutch inspected by a expert.",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7444b6940001e8c703a",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99913964d15e001edd7c04",
#                                 "name": "Rubbing/Polishing"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Cluctch+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Clutch+1.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fcc9610561f56001e20e9b0",
#                                 "name": "Clutch"
#                             },
#                             {
#                                 "_id": "5fcc961e561f56001e20e9b1",
#                                 "name": "Clutch Fluid Leak"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5fc351cfce84d6001eaee523",
#                         "subServiceName": "Electricals",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Electricals.png",
#                         "description": "One of the most essential systems of a car is its electrical system; from the battery to the wiring. This system is what provides power to other parts of the vehicle and hence aptly named, ‘the powerhouse’ of the vehicle.  If you are unable to turn on your car, or don’t hear the grinding of the ignition, call AutoFlipz’s trained technicians to assist you with any car electrical repair services you might need.",
#                         "brief": "Get the powerhouse of your car inspected. ",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa2864d15e001edd7c2b",
#                                 "name": "Injector Cleaning"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/electric+1.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Electric+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fd5c956b2232e001e61fb67",
#                                 "name": "Electrical System"
#                             },
#                             {
#                                 "_id": "5fd5c964b2232e001e61fb68",
#                                 "name": "Battery "
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5fc35200ce84d6001eaee524",
#                         "subServiceName": "Engine",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/ENgine+%26+Basic+Service.jpg",
#                         "description": "To ensure smooth functioning of the vehicle’s engine, you must get your vehicle’s engine looked after by AutoFlipz's experts as and when suggested by the manufacturer. If you do end up in a situation where our vehicle requires undue repair or replacement of engine, then our AutoFlipz's technicians can offer best in-class services for the same.",
#                         "brief": "The engine is arguable the most important, and intricate, aspect of your car. ",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fcf28bf561f56001e20e9e9",
#                                 "name": "Interior Vacuuming"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a506ce84d6001eaee534",
#                                 "name": "Radiator Flushing"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa2864d15e001edd7c2b",
#                                 "name": "Injector Cleaning"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Engine+1.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Engine+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fb78dedb66787001e93b355",
#                                 "name": "Engine "
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5fc3522fce84d6001eaee525",
#                         "subServiceName": "Fuel System",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Fuel+System.png",
#                         "description": "Is your car engine making an unusual sound and you can’t pinpoint what it is? Your fuel pump may be damaged or your fuel filter could be clogged. Bring your car to any one of our AutoFlipz workshops or call us any time at all. We at AutoFlipz, can help you figure out the issue and offer all appropriate assistance to solve the issue, while maintaining the quality of the services provided to you.",
#                         "brief": "A fully operational fuel system allows the engine to perform at its best.",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa6764d15e001edd7c2c",
#                                 "name": "Throttle Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a506ce84d6001eaee534",
#                                 "name": "Radiator Flushing"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Fuel+System+1.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Fuel+System+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fd5d48db2232e001e61fb6a",
#                                 "name": "No-start"
#                             },
#                             {
#                                 "_id": "5fd5d4a8b2232e001e61fb6b",
#                                 "name": "Performance-related"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5fc3525cce84d6001eaee526",
#                         "subServiceName": "Suspension",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Suspension.jpg",
#                         "description": "Is the front of your car dipping downwards when you hit the brake? Is there a noise while driving on rough roads? Is your car swayed by sideward winds? Is there something wrong with the handling? If any of this is True, you probably have something wrong in your car’s suspension.  If not repaired on time, issues with the suspension system may reduce the stability of the vehicle and the driver could lose control. Hence AutoFlipz recommends that you get your suspensions components checked at the first hint of a problem.",
#                         "brief": "Your car’s suspension is generally out of sight and out of mind, but it plays a crucial role.",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99913964d15e001edd7c04",
#                                 "name": "Rubbing/Polishing"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fcf28bf561f56001e20e9e9",
#                                 "name": "Interior Vacuuming"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Suspension.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fd5d688b2232e001e61fb6c",
#                                 "name": "Front Shocker"
#                             },
#                             {
#                                 "_id": "5fd5d699b2232e001e61fb6d",
#                                 "name": "Rear Shocker"
#                             },
#                             {
#                                 "_id": "5fd5d6afb2232e001e61fb6e",
#                                 "name": "Shocker Mount"
#                             },
#                             {
#                                 "_id": "5fd5d6bcb2232e001e61fb6f",
#                                 "name": "Link Rod"
#                             },
#                             {
#                                 "_id": "5fd5d6ddb2232e001e61fb70",
#                                 "name": "Jumping Rod Bush"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5fc3528cce84d6001eaee527",
#                         "subServiceName": "Steering ",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Steering.jpg",
#                         "description": "Along with the suspension system, the steering is the device responsible for the amount of control a driver has over the vehicle. If your steering feels heavy, or makes noises, or vibrates, make sure you take the vehicle for evaluation by AutoFlipz's experts.  The Staff at any of AutoFlipz’s outlets can assist you with steering related issues with ease.",
#                         "brief": "Go right. Go left. The steering system is what controls the direction of the wheels. ",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Steering+1.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Steering+2.gif"
#                         ],
#                         "components": []
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5fc352bbce84d6001eaee528",
#                         "subServiceName": "Transmission",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Transmission.jpg",
#                         "description": "Issues in transmission lead to unusual sounds, gear slipping, hard shifting and various other serious intrusions while driving.  AutoFlipz Services help you be on guard for such potential disruptions. Technicians at AutoFlipz provide world class transmission repair services in our workshops.",
#                         "brief": "Avoid costly transmission repairs.",
#                         "serviceId": "5f980e1a99fd6b127b820cae",
#                         "serviceName": "Inspection",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Inspection+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a506ce84d6001eaee534",
#                                 "name": "Radiator Flushing"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa6764d15e001edd7c2c",
#                                 "name": "Throttle Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99aa2864d15e001edd7c2b",
#                                 "name": "Injector Cleaning"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/T1.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/T2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fd8796fb2232e001e61fb7e",
#                                 "name": "Transmission"
#                             },
#                             {
#                                 "_id": "5fd878ddb2232e001e61fb7d",
#                                 "name": "Transmission Fluid"
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "serviceId": "5f980d6f99fd6b127b820cac",
#                 "serviceName": "Wheel Service",
#                 "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Wheel+Service+Head.jpg",
#                 "subServices": [
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5f9993b764d15e001edd7c07",
#                         "subServiceName": "Wheel Rotation",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Wheel+Service+Head.jpg",
#                         "description": "Rotating tyres prevents tyres from uneven wear. It will make your ride smoother and handling safer. Tyre rotations extends the life of your tyres, saving you time and money in the long run. Everyone knows that wheels are expensive. Therefore, it is best to make sure they continue to function well. To ensure your safety as well as the health of your cars tyres, we at AutoFlipz offer Wheel Rotation service at your convenience.",
#                         "brief": "Prolong your car's tyre life.",
#                         "serviceId": "5f980d6f99fd6b127b820cac",
#                         "serviceName": "Wheel Service",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Wheel+Service+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7444b6940001e8c703a",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/WheelRotation.jpg",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Wheel+Alignment.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fa119b4e0d0e5001ef63159",
#                                 "name": "All Four Tyre"
#                             },
#                             {
#                                 "_id": "5fa119d6e0d0e5001ef6315a",
#                                 "name": "Depth "
#                             },
#                             {
#                                 "_id": "5fa119e0e0d0e5001ef6315b",
#                                 "name": "Pattern"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5f99949064d15e001edd7c09",
#                         "subServiceName": "Wheel Alignment",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/WA.jpg",
#                         "description": "Wheels get damaged from a variety of causes including bad roads and potholes, leading to misalignment. Misaligned tyres are much more likely to premature wear and tear. It is of utmost importance that car owners get wheel alignment checks to prolong the life of their car’s tyres as much as possible. AutoFlipz specializes in car wheel alignment wherein our experts use the latest technology and best equipment to check for faulty alignment and then fix it. Proper car wheel alignment ensures the durability of the wheels, a smooth and safe drive for your car, and major savings on fuel. So get your vehicle’s wheel alignment checked as soon as possible.",
#                         "brief": "Proper wheel alignment helps in better handling and improves the car's stability and life.",
#                         "serviceId": "5f980d6f99fd6b127b820cac",
#                         "serviceName": "Wheel Service",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Wheel+Service+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7444b6940001e8c703a",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fcf28bf561f56001e20e9e9",
#                                 "name": "Interior Vacuuming"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Wheel+Alignment.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/ALignment.jpg"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fa11ae2e0d0e5001ef6315c",
#                                 "name": "Laser Assisted "
#                             },
#                             {
#                                 "_id": "5fa11b0ae0d0e5001ef6315d",
#                                 "name": "Wheel Rigidity"
#                             },
#                             {
#                                 "_id": "5fa11b43e0d0e5001ef6315e",
#                                 "name": "Camber & Castor"
#                             },
#                             {
#                                 "_id": "5fa11b9ce0d0e5001ef6315f",
#                                 "name": "Steering "
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "299",
#                         "subServiceId": "5f9993ea64d15e001edd7c08",
#                         "subServiceName": "Wheel Balancing",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Wheel+Balancing.jpg",
#                         "description": "You’ll know if your car requires wheel balancing if your steering wheel is rocking back and forth as you drive. If you notice this in your car, you must immediately call AutoFlipz as driving with wheels that require balancing can be very dangerous. The vibrations caused by imbalanced wheels can also put pressure on the lower ball joints, axles and other crucial parts of your car. The increased pressure can also cause the wear and tear rate of these parts to increase, adding to maintenance problems of your car. AutoFlipz's technicians recommend tyre balancing as soon as you get new tyres for your car. This would ensure that all of the tyres have equal wheel weights.",
#                         "brief": "Get your wheels balanced and ensure optimum performance.",
#                         "serviceId": "5f980d6f99fd6b127b820cac",
#                         "serviceName": "Wheel Service",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Wheel+Service+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a506ce84d6001eaee534",
#                                 "name": "Radiator Flushing"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Wheel+Balancing.jpg",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Wheel+Alignment.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fa11ebce0d0e5001ef63160",
#                                 "name": "Automated "
#                             },
#                             {
#                                 "_id": "5fa11ed2e0d0e5001ef63161",
#                                 "name": "Weight"
#                             },
#                             {
#                                 "_id": "5fa11f02e0d0e5001ef63162",
#                                 "name": "Alloy Weights"
#                             },
#                             {
#                                 "_id": "5fa11b0ae0d0e5001ef6315d",
#                                 "name": "Wheel Rigidity"
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "serviceId": "5f980d22fd4d11125434a766",
#                 "serviceName": "Dent/Paint",
#                 "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                 "subServices": [
#                     {
#                         "addedToCart": False,
#                         "price": "17999",
#                         "subServiceId": "5f9995bf64d15e001edd7c0c",
#                         "subServiceName": "Full Body ",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Full+Body.png",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Full Body dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99967664d15e001edd7c0e",
#                         "subServiceName": "Front Bumper",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Front+Bumper.jpeg",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Front Bumper dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99975364d15e001edd7c10",
#                         "subServiceName": "Bonnet",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Bonnet+Paint.jpeg",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Bonnet dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f9996d964d15e001edd7c0f",
#                         "subServiceName": "Rear Bumper",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Rear+Bumper+Paint.png",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Rear Bumper dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99985b64d15e001edd7c11",
#                         "subServiceName": "Boot Bumper",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Boot+.png",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Boot  Bumper /ndent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f999ff764d15e001edd7c14",
#                         "subServiceName": "Left Fender",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Left+Fender+Paint.png",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Left Fender dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a06464d15e001edd7c15",
#                         "subServiceName": "Right Fender",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Right+Fender+paint.png",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Right Fender dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a0cb64d15e001edd7c16",
#                         "subServiceName": "Right Front Door",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Right+Front+Door.jpeg",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Front door dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a11a64d15e001edd7c17",
#                         "subServiceName": "Left Front Door",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Left+front+door.jpg",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Front door dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a16864d15e001edd7c18",
#                         "subServiceName": "Right Rear Door",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Rear+Right+door.jpeg",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Rear Door dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a5d864d15e001edd7c19",
#                         "subServiceName": "Left Rear Door",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Sub+Heads/Rear+left+door.jpeg",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Rear Door dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a61b64d15e001edd7c1a",
#                         "subServiceName": "Left Quater Panel",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Left+Quater+Panel.png",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Quarter Panel dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a65064d15e001edd7c1b",
#                         "subServiceName": "Right Quater Panel",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/DSC_0059.png",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Quarter Panel dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a6a064d15e001edd7c1c",
#                         "subServiceName": "Left Running Board",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Left+Running+board.jpg",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Running board dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "2199",
#                         "subServiceId": "5f99a6fe64d15e001edd7c1d",
#                         "subServiceName": "Right Running Board",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/Right+Running+Board.png",
#                         "description": "A dent here, a ding there. Driving in India is no less than a challenge. Unfortunately, accidents happen that can cause damage to the vehicle in terms of paint damage and dent. Paint scratches and dents shows detract from the appearance of your car. A car with dents and scratches holds less value in the resale market. Also ignoring paint damage can cause rusting problems. AutoFlipz specialises in car dent repair and car painting services for all makes and models. If you wish to get rid of those scratches and dents on your car, call us today or book online.",
#                         "brief": "Running board dent repair & painting.",
#                         "serviceId": "5f980d22fd4d11125434a766",
#                         "serviceName": "Dent/Paint",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/DP+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5f99962964d15e001edd7c0d",
#                                 "name": "Alloy Paint (All Four)"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting+2.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Denting.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faeca42041f0f001e0d226a",
#                                 "name": "Grade A"
#                             },
#                             {
#                                 "_id": "5faeca63041f0f001e0d226b",
#                                 "name": "4 Layers"
#                             },
#                             {
#                                 "_id": "5faeca7b041f0f001e0d226c",
#                                 "name": "DuPont "
#                             },
#                             {
#                                 "_id": "5faeca92041f0f001e0d226d",
#                                 "name": "Rubbing & Polishing"
#                             },
#                             {
#                                 "_id": "5fba259d81eb8d001e7e7f8f",
#                                 "name": "Cathodic-e"
#                             },
#                             {
#                                 "_id": "5fba25dc81eb8d001e7e7f90",
#                                 "name": "Base & Clear"
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "serviceId": "5f980d43c5ea02126c69db14",
#                 "serviceName": "AC Service",
#                 "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/AC+Head.jpg",
#                 "subServices": [
#                     {
#                         "addedToCart": False,
#                         "price": "1049",
#                         "subServiceId": "5f9994f464d15e001edd7c0a",
#                         "subServiceName": "AC Checkup & Gas Fill",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Edited/AC+Checkup.png",
#                         "description": "Air Conditioning is an important comfort feature in today's  Cars.  Beat the heat in summers with our AC Checkup & Gas Topup package. At AutoFlipz, we offer the best car AC Checkup & Repair services at best prices in Industry which include compressor check, fixing refrigerant leaks and gas top up to restore the performance of the AC.",
#                         "brief": "Keep your Car AC in top condition.",
#                         "serviceId": "5f980d43c5ea02126c69db14",
#                         "serviceName": "AC Service",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/AC+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a4e6ce84d6001eaee533",
#                                 "name": "AC Filter"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7444b6940001e8c703a",
#                                 "name": "Spark Plugs"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99913964d15e001edd7c04",
#                                 "name": "Rubbing/Polishing"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/AC.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5fa10ca3e0d0e5001ef63149",
#                                 "name": "AC Gas"
#                             },
#                             {
#                                 "_id": "5fa10d0ce0d0e5001ef6314a",
#                                 "name": "AC Filter"
#                             },
#                             {
#                                 "_id": "5fa10d1ee0d0e5001ef6314b",
#                                 "name": "AC"
#                             },
#                             {
#                                 "_id": "5fa10d47e0d0e5001ef6314d",
#                                 "name": "AC Vent"
#                             },
#                             {
#                                 "_id": "5fa10d2fe0d0e5001ef6314c",
#                                 "name": "Condenser "
#                             },
#                             {
#                                 "_id": "5fba23ae81eb8d001e7e7f8d",
#                                 "name": "Gas Leakage"
#                             },
#                             {
#                                 "_id": "5fba23c781eb8d001e7e7f8e",
#                                 "name": "Blower"
#                             }
#                         ]
#                     },
#                     {
#                         "addedToCart": False,
#                         "price": "1899",
#                         "subServiceId": "5f99954864d15e001edd7c0b",
#                         "subServiceName": "Complete AC Service",
#                         "logo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/Complete+AC.png",
#                         "description": "Good climate control is essential for your vehicle if you want to enjoy a comfortable ride. AC systems require maintenance to continue functioning well. With proper maintenance, the AC should provide long-term service. The key benefits are efficient cool air in summer and in winter it provides warm dehumidified air & also provide a pleasant and odor free environment at all times. At AutoFlipz workshop, our trained and experienced technicians check for all potential faults associated with the car AC system like leaks and faulty compressors. We then repair or replace the damaged parts to ensure that your car AC is working in excellent condition so you can enjoy your driving experience in any kind of weather.",
#                         "brief": "Beat the heat in Summers.",
#                         "serviceId": "5f980d43c5ea02126c69db14",
#                         "serviceName": "AC Service",
#                         "serviceLogo": "https://storageautoflipz.s3.ap-south-1.amazonaws.com/Sub+Head+Logo/AC+Head.jpg",
#                         "defaultAddOns": [],
#                         "additionalAddOns": [
#                             {
#                                 "images": [],
#                                 "_id": "5fe1aaba1b4b84001f8893b5",
#                                 "name": "Insurance Renewal Assistance"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc3a4e6ce84d6001eaee533",
#                                 "name": "AC Filter"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dry+Cleaning+2.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                                 ],
#                                 "_id": "5f99933464d15e001edd7c06",
#                                 "name": "Interior Dry Cleaning"
#                             },
#                             {
#                                 "images": [],
#                                 "_id": "5fc7e7cc4b6940001e8c703c",
#                                 "name": "Alloy Cleaning"
#                             },
#                             {
#                                 "images": [
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/User+App+Pictures/Car+Wash.gif",
#                                     "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Vacuuming.gif"
#                                 ],
#                                 "_id": "5f99907f64d15e001edd7c02",
#                                 "name": "Car Wash"
#                             }
#                         ],
#                         "serviceImages": [
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/AC.gif",
#                             "https://storageautoflipz.s3.ap-south-1.amazonaws.com/New+Icons/Videos/Dashboard+Polishing.gif"
#                         ],
#                         "components": [
#                             {
#                                 "_id": "5faec222041f0f001e0d2268",
#                                 "name": "AC Gas Replacement"
#                             },
#                             {
#                                 "_id": "5faec8c9041f0f001e0d2269",
#                                 "name": "Compressor Oil Topup"
#                             },
#                             {
#                                 "_id": "5fa10d2fe0d0e5001ef6314c",
#                                 "name": "Condenser "
#                             },
#                             {
#                                 "_id": "5fa10d47e0d0e5001ef6314d",
#                                 "name": "AC Vent"
#                             },
#                             {
#                                 "_id": "5fa10e75e0d0e5001ef63153",
#                                 "name": "Dashboard"
#                             },
#                             {
#                                 "_id": "5fa10e90e0d0e5001ef63154",
#                                 "name": "Dashboard"
#                             },
#                             {
#                                 "_id": "5fa10eb6e0d0e5001ef63155",
#                                 "name": "Cooling Coil"
#                             },
#                             {
#                                 "_id": "5fa10f7fe0d0e5001ef63157",
#                                 "name": "AC Leak"
#                             },
#                             {
#                                 "_id": "5fa10f74e0d0e5001ef63156",
#                                 "name": "AC Filter"
#                             },
#                             {
#                                 "_id": "5fba23c781eb8d001e7e7f8e",
#                                 "name": "Blower"
#                             },
#                             {
#                                 "_id": "5fba23ae81eb8d001e7e7f8d",
#                                 "name": "Gas Leakage"
#                             }
#                         ]
#                     }
#                 ]
#             }
#         ]
#     }
#
#
#
# app1.run(host='0.0.0.0', port=5001)