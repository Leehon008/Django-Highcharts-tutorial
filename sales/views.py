from django.shortcuts import render
import pandas as pd


# Create your views here.
def home(request):
    """ view function for sales app """

    # read data
    use_cols = ["Manufacturer", "Model", "Sales in thousands", "4-year resale value", "Vehicle type",
                "Price in thousands", "Engine size", "Horsepower", "Wheelbase", "Width", "Length", "Curb weight",
                "Fuel capacity", "Fuel efficiency", "Latest Launch"]
    df = pd.read_csv("data/car_sales.csv", usecols=use_cols)
    # df = pd.read_csv("data/car_sales.csv")
    rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    table_content = df.to_html(index=None)

    table_content = table_content.replace("", "")
    table_content = table_content.replace('class="dataframe"', "class='table table-striped'")
    table_content = table_content.replace('border="1"', "")

    context = {"categories": categories, 'values': values, 'table_data': table_content}
    return render(request, 'index.html', context=context)
