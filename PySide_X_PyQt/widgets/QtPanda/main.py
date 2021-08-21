import sys

import pandas as pd
from PyQt5.QtWidgets import QApplication
from QtPandas.QtPandas import QDataFrame

if __name__ == "__main__":
    app = QApplication()
    df = pd.read_csv("all_months.csv")
    qdf = QDataFrame(df)
    qdf.show()
    sys.exit(app.exec_())
