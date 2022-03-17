#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import json
import os.path


def get_product(prds, name, shop, cost):
    """
    Добавить данные.
    """
    prds.append(
        {
            "name": name,
            "shop": shop,
            "cost": cost
        }
    )
    return prds


def display_products(products):
    if products:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Наименование товара",
                "Название магазина",
                "Стоимость"
            )
        )
        print(line)

        for idx, product in enumerate(products, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<15} |'.format(
                    idx,
                    product.get('name', ''),
                    product.get('shop', ''),
                    product.get('cost', 0)
                )
            )
        print(line)

    else:
        print("Список продуктов пуст")


def save_products(file_name, prds):
    """
    Сохранить все записи в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(prds, fout, ensure_ascii=False, indent=4)


def load_products(file_name):
    """
    Загрузить все записи из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


@click.command()
@click.argument('command')
@click.argument('filename')
@click.option('--name', prompt='Name',
              help='The product`s name'
)
@click.option('--shop', prompt='Shop', help='The shop that has the product')
@click.option('--cost', prompt='Cost', help='The product`s cost')
def main(command, filename, name, shop, cost):
    """
    Главная функция программы
    """
    is_dirty = False
    if os.path.exists(filename):
        products = load_products(filename)
    else:
        products = []
    if command == "add":
        products = get_product(
            products,
            name,
            shop,
            cost
        )
        is_dirty = True
    elif command == "display":
        display_products(products)

    if is_dirty:
        save_products(filename, products)


if __name__ == '__main__':
    main()