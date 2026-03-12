from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from ui_widget import Ui_widget
from ui_homeWidget import Ui_homeWidget
from random import shuffle

waterTermToDef = {
    "Eutrophication": "Nutrient runoff that creates\n\"Dead Zones\" by starving\nwater of oxygen",
    "Microplastics": "Tiny plastic debris that\nenters the food chain and\nnever fully biodegrades",
    "Non-Point Source": "Pollution from broad areas\n(like city streets or farms)\nrather than one pipe",
    "Turbidity": "The measure of water clarity;\nhigh levels can choke fish\nand block sunlight",
    "Pathogens": "Disease-causing bacteria from\nuntreated sewage or\nanimal waste",
    "Bioaccumulation": "The process where waste builds\nup in large amounts as they\nmove up the food chain"
}
airTermToDef = {
    "Particulate Matter": "Tiny solid or liquid droplets\n(like soot or dust) that can\nbe inhaled into the lungs",
    "Ground-Level Ozone": "A colorless gas created by\nchemical reactions that acts as\nthe main ingredient in smog",
    "Carbon Monoxide": "An odorless, colorless gas\nfrom car exhaust that prevents\nblood from carrying oxygen",
    "Acid Rain": "Precipitation containing\nharmful levels of nitric and\nsulfuric acids from fossil fuels",
    "Greenhouse Gases": "Substances like CO2 and\nmethane that trap heat in the\natmosphere, causing warming",
    "Volatile Organic Compounds": "Chemicals from paints or\ncleaners that \"off-gas\" and\nlower indoor air quality"
}
lightTermToDef = {
    "Skyglow": "The brightening of the\nnight sky over inhabited\nareas, hiding the stars",
    "Light Trespass": "When unwanted artificial\nlight shines onto a property\nwhere it is not needed",
    "Glare": "Excessive brightness that\ncauses visual discomfort or\nreduces visibility for drivers",
    "Circadian Rhythm": "The internal 24-hour clock\n\"reset\" by light that\nregulates sleep in humans",
    "Clutter": "Bright, confusing, and\nexcessive groupings of light\nsources (like Times Square)",
    "Phototaxis": "The bodily movement of an\norganism (like a sea turtle)\ntoward or away from light"
}

class HomeWidget(QWidget, Ui_homeWidget):
    def __init__(self, waterWindow, airWindow, lightWindow):
        super().__init__()
        self.setupUi(self)

        self.waterButton.clicked.connect(waterWindow.show)
        self.airButton.clicked.connect(airWindow.show)
        self.lightButton.clicked.connect(lightWindow.show)

class Widget(QWidget, Ui_widget):
    def __init__(self, topic):
        super().__init__()
        self.setupUi(self)

        self.alreadySelected: int = 0
        self.selectedItems = []
        self.correctItems = []

        self.shuffledList = self.shuffleLists(topic)
        self.headerImg.setPixmap(QPixmap(f":/Images/{topic} banner.png"))

        for i in range(12):
            targetButton: QPushButton = getattr(self, f"item_{i+1}")
            targetButton.clicked.connect(lambda checked=False, index=i: self.buttonClicked(index))

    def shuffleLists(self, topic):
        topicToList: dict = {
            "water": waterTermToDef,
            "air": airTermToDef,
            "light": lightTermToDef
        }
        self.targetDict = topicToList[topic]
        keysList = list(self.targetDict.keys())
        valuesList = list(self.targetDict.values())
        combinedList = keysList + valuesList
        shuffle(combinedList)
        return combinedList

    def buttonClicked(self, i):
        self.alreadySelected += 1

        if self.alreadySelected > 2:
            self.alreadySelected = 1
            self.selectedItems = []
            for buttonI in range(12):
                targetButton: QPushButton = getattr(self, f"item_{buttonI + 1}")
                if not (targetButton.text() in self.correctItems):
                    targetButton.setText("")

        targetButton: QPushButton = getattr(self, f"item_{i+1}")
        targetButton.setText(self.shuffledList[i])

        self.selectedItems.append(self.shuffledList[i])

        if self.alreadySelected == 2:
            firstItem = self.selectedItems[0]
            secondItem = self.selectedItems[1]
            if (self.targetDict.get(firstItem, None) == secondItem) or (self.targetDict.get(secondItem, None) == firstItem):
                for item in self.selectedItems:
                    self.correctItems.append(item)

        if len(self.correctItems) == 12:
            QMessageBox.information(self, "Victory!", "You win!")
            self.close()

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication()

    waterWindow = Widget("water")
    airWindow = Widget("air")
    lightWindow = Widget("light")
    homeWindow = HomeWidget(waterWindow, airWindow, lightWindow)
    homeWindow.show()

    app.exec()