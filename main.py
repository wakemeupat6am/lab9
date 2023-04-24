import os
from os import listdir, path
from PIL import Image, ImageFilter
import csv

def prog1(input_dir, output_dir='processed_images'):

    for file in os.listdir(input_dir):
        if file.endswith(".png") or file.endswith(".jpg"):
            os.makedirs(output_dir, exist_ok=True)
            fullpath = path.join(input_dir, file)
            output_fullpath = path.join(output_dir, file)
            with Image.open(fullpath) as im:
                processed_image = im.filter(ImageFilter.BoxBlur(50))
                processed_image.save(output_fullpath)


def prog2(input_file):
    total_cost = 0
    with open(input_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            product_name = row[0]
            product_amount = int(row[1])
            product_cost = int(row[2])
            print(product_name, '-', product_amount, 'шт за', product_cost, 'рублей')
            total_cost += product_cost * product_amount
    print('Итоговая сумма -', total_cost, 'рублей')


prog1('images')
prog2('data.csv')