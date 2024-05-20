from datetime import datetime
import json
from unidecode import unidecode
import os
import hashlib
def calculate_check_digit(data):
    weights = [
        7,
        3,
        1,
        7,
        3,
        1,
        7,
        3,
        1]
    total = 0
    for i, char in enumerate(data):
        weight = weights[i % len(weights)]
        if char.isdigit():
            total += int(char) * weight
            continue
        if char.isalpha():
            total += ((ord(char.upper()) - ord('A')) + 10) * weight
            continue
        total += 0 * weight
    check_digit = total % 10
    return check_digit
def format_name(input_name):
    formatted_name = unidecode(input_name).upper()
    return formatted_name
def generate_mrz_string(ma, ten, ngay_sinh, ngay_het_han, gioi_tinh):
    try:
        line1 = 'IDVNM{}{}{}<<{}'.format(ma[3:12], calculate_check_digit(ma[3:12]), ma, calculate_check_digit(ma))
        ten = format_name(ten)
        ngay_sinh_formatted = datetime.strptime(ngay_sinh, '%d/%m/%Y').strftime('%y%m%d')
        ngay_het_han_formatted = datetime.strptime(ngay_het_han, '%d/%m/%Y').strftime('%y%m%d')
        gioi_tinh_code = 'M' if gioi_tinh.lower() == 'nam' else 'F'
        line2 = '{}{}{}{}{}VNM<<<<<<<<<<<{}'.format(ngay_sinh_formatted, calculate_check_digit(ngay_sinh_formatted), gioi_tinh_code, ngay_het_han_formatted, calculate_check_digit(ngay_het_han_formatted), '')
        line2 = '{}{}{}{}{}VNM<<<<<<<<<<<{}'.format(ngay_sinh_formatted, calculate_check_digit(ngay_sinh_formatted), gioi_tinh_code, ngay_het_han_formatted, calculate_check_digit(ngay_het_han_formatted), calculate_check_digit(line1[5:30] + line2[0:7] + line2[8:15] + line2[18:29]))
        parts = ten.split()
        ho = parts[0]
        if len(parts) > 1:
            ten = '<'.join(parts[1:])
        else:
            ten = parts[0]
        line3 = f'''{ho}<<{ten}<<<<<<<<<<<<<<<'''
        line3 += '<' * (30 - len(line3))
        return f'''{line1}\n{line2}\n{line3[:30]}'''
    except:return None
