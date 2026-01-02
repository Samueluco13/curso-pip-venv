import matplotlib.pyplot as plt

def generate_pie_chart(labels, values, title):
    fig, ax = plt.subplots()
    fig.suptitle(title)
    ax.pie(values, labels = labels)
    plt.savefig(f"{title}.png")