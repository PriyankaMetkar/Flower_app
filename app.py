import streamlit as st
st.title("My First Application")
st.write("I am testing streamlit")
st.image("flower Image.gif")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['target'] = iris.target

# Create a dictionary to map target values to flower names
target_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
data['flower_name'] = data['target'].map(target_names)

# Define the Streamlit app
def main():
    st.title("Iris Flower Visualization")

    # Sidebar for filtering
    st.sidebar.header("Filters")
    flower_name_filter = st.sidebar.selectbox("Select Flower Name", data["flower_name"].unique())

    # Filtered dataframe based on user selections
    filtered_df = data[data["flower_name"] == flower_name_filter]

    # Display filtered flowers
    st.header("Filtered Flowers")
    for index, row in filtered_df.iterrows():
        st.subheader(row["flower_name"])
        st.write("Sepal Length:", row["sepal length (cm)"])
        st.write("Sepal Width:", row["sepal width (cm)"])
        st.write("Petal Length:", row["petal length (cm)"])
        st.write("Petal Width:", row["petal width (cm)"])

    # Visualizations
    st.header("Visualizations")
    st.subheader("Sepal Length vs. Sepal Width")
    sns.scatterplot(x="sepal length (cm)", y="sepal width (cm)", data=filtered_df)
    plt.title("Sepal Length vs. Sepal Width")
    st.pyplot()

    st.subheader("Petal Length vs. Petal Width")
    sns.scatterplot(x="petal length (cm)", y="petal width (cm)", data=filtered_df)
    plt.title("Petal Length vs. Petal Width")
    st.pyplot()

if __name__ == "__main__":
    main()