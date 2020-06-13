#!/usr/bin/env python3
def get_token():
    token = ""
    with open("token", "r") as file:
        token = file.readlines()
    return token[0].replace("\n", "")
