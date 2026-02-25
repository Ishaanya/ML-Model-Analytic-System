import pandas as pd 

def load_data(base_path = "/home/ishanya-poddar/Desktop/Projects/ML + NLP/ML&NLP/Datasets/Raw Datasets"):
    orders = pd.read_csv("/home/ishanya-poddar/Desktop/Projects/ML + NLP/ML&NLP/Datasets/Raw Datasets/olist_orders_dataset.csv")
    order_items = pd.read_csv("/home/ishanya-poddar/Desktop/Projects/ML + NLP/ML&NLP/Datasets/Raw Datasets/olist_order_items_dataset.csv")
    customers = pd.read_csv("/home/ishanya-poddar/Desktop/Projects/ML + NLP/ML&NLP/Datasets/Raw Datasets/olist_customers_dataset.csv")
    reviews = pd.read_csv("/home/ishanya-poddar/Desktop/Projects/ML + NLP/ML&NLP/Datasets/Raw Datasets/olist_order_reviews_dataset.csv")
    products = pd.read_csv("/home/ishanya-poddar/Desktop/Projects/ML + NLP/ML&NLP/Datasets/Raw Datasets/olist_products_dataset.csv")

    return orders, order_items, customers, reviews, products

def merge_data(orders, order_items, customers, reviews, products):
    df = order_items.merge(orders, on = "order_id", how = "left")
    df = df.merge(customers, on = "customer_id", how = "left")
    df = df.merge(reviews, on = "order_id", how = "left")
    df = df.merge(products, on = "product_id", how = "left")

    return df

def create_order_total(df):
    order_total = df.groupby("order_id")["price"].sum().reset_index()
    order_total.rename(columns = {"price" : "order_total_price"}, inplace = True)
    df = df.merge(order_total, on = "order_id", how = "left")
    return df     