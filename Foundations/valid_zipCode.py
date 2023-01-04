def valid_zipcode(zip_code):
    return len(zip_code) == 6 and zip_code.isdigit()

ans = valid_zipcode("41300")
print(ans)