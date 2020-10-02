import sys
import pandas as pd

from PySide2.QtWidgets import QApplication
from QtPandas.QDataFrame import QDataFrame

if __name__ == "__main__":
    app = QApplication()
    df = pd.read_csv("data.csv")
    qdf = QDataFrame(df)
    qdf.show()
    sys.exit(app.exec_())
