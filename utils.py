from flask import Flask, jsonify, request
import base64
from bd_config import db
import json


# def validate_json(input_json,caller):
#     message = ""
#     code = 404
#     if caller == "group":
#         if input_json['name'] == "":
#             message = "Se requiere un nombre para el grupo"
#         elif input_json['level'] == "":
#             message = "Se requiere un nivel para el grupo"
#         elif input_json['capacity'] == "" or input_json['capacity'] == 0:
#             capacity = 30
#         else:
#             code = 200
#     new_group = Group(
#         name = input_json['name'],
#         level = input_json['level'],
#         capacity = input_json['capacity']
#     )
#     return message,code,new_group
# def validate_json(input_json,caller): 
#     message = ""

#         if input_json['name'] == "" or input_json['last_name'] == "" :
#             message = "Name o Apellido es requerido"
#         if input_json['age'] == "":
#             message = "Edad es requerido"
#         if input_json['email'] == "":
#             message = "Email es requerido"
        
        

     

#     if caller == "group":
#         message = ""
#         response_code = 0
#         new_group = Group()
#         uuid  =  ""
#         print(str(input_json))
#         if input_json['name']!="" and input_json['level']!="":
#                 message = "ok"
#                 response_code = 200
#         elif input_json['name']=="":
#                 message = "Nombre Grupo Necesario"
#                 response_code = 400
#         else:
#                 message = "Nivel Grupo Necesario"
#                 response_code = 400
#         uuid  = generate_uuid(input_json['name'],input_json['level'])
#         new_group.group_name = input_json['name']
#         new_group.group_level = input_json['level']
#         new_group.group_capacity = 45
#         new_group.group_uuid = uuid
#         db.session.add(new_group)
#         db.session.commit()
#         return new_group,response_code,message

# def validate_role_json(role):

#     get_role = db.session.execute(f"select * from roles where role_name = '{role}' limit 1;")
#     if get_role.name == role:
#         return int(get_role.fetchone().id)
#     else:
#         db.session.execute(f"insert into roles (role_name) values ('{role}');")
#         db.session.commit()
#     return int(db.session.execute(f"select id from roles where role_name = '{role}' limit 1;").fetchone()[0].id)
    
    
# def validate_group_jsong(group):
    
#     query = "SELECT * FROM `groups` WHERE group_name = '{group}';"
#     print(query)
#     list_group = []
#     list_group = db.session.execute(query)
#     for i in list_group:
#         print(i.id)

#     if list_group.rowcount > 0:
#         return int(get_group.fetchone()[0].id)
#     else:
#         query = f"INSERT INTO `groups`(group_name) values ('{group}');"
#         db.session.execute(query)
#         db.session.commit()
        
#     return int(db.session.execute(f"select id from `groups` where group_name = '{group}';").fetchone()[0].id)




# def generate_uuid(name,level):
#      uuid = ""
#      uuid+=name
#      uuid+="-" 
#      uuid+=level
#      return uuid