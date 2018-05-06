# Create a class to hold data
import pyautogui as pag

# form = {}


class Movement:
    specialCases = ['Boxes', 'Weight']

    def __init__(self, shipObj):
        if isinstance(shipObj, Shipment):
            self.shipObj = shipObj
        else:
            raise Exception('Passed object is not a Shipment instance.')

    def special_case_move(self, coordObj):
        '''
        param1: Coordinate object located within Shipment object
        use: Double clicks and inputs a value into a scroll box.
        '''
        pag.moveTo(coordObj.x, coordObj.y, duration=0.25)
        pag.moveRel(-8, 0)
        pag.doubleClick(interval=0.25)
        pag.typewrite(coordObj.val)
        print('Special case executed!')

    def normal_move(self, coordObj):
        '''
        param1: Coordinate object located within Shipment object
        use: Clicks and inputs a value (coordObj.val) into an input box.
        '''
        pag.moveTo(coordObj.x, coordObj.y, duration=0.25)
        pag.click()
        pag.typewrite(coordObj.val)

    def determine_move_mode(self):
        for coordObj in self.shipObj.coordinates:
            if coordObj.name in self.specialCases:
                self.special_case_move(coordObj)
            else:
                self.normal_move(coordObj)


class Shipment:

    hazmatCodes = [
        'cao', 'eli', 'rcm', 'req', 'rfg',
        'rfl', 'rli', 'rmd', 'rng', 'rox'
        ]

    coords = {
        'Ship Via': (580, 235), 'Ship From': (415, 351),
        'Ship To': (576, 351), 'Airwaybill': (831, 236),
        'Flight': (412, 279), 'Boxes': (465, 276),
        'Weight': (664, 280),
        }

    def __init__(self):
        self.shc = ['svc', 'pri']
        self.shipper = 'seajj'
        self.hazmat = False
        self.charges = 'nc'
        self.product = 'pri'
        self.natureOfGoods = 'Aircraft parts'
        self.coordinates = []
        self.run()

    def add_shc(self):
        addons = input('Input additional SHCs. separate with commas. \n')  # make parameter eventually
        if addons:
            addons = addons.split()
            for item in addons:
                if item in self.hazmatCodes:
                    self.shc.append(item.strip())
                else:
                    continue
        return

    def run(self):  # temp use to run. doesn't fit in with workflow right now.
        for key, values in self.coords.items():
            (x, y) = values
            self.coordinates.append(Coordinates(key, x, y))


class Coordinates:
    '''
    Create a template for calling preloaded coordinates
    '''
    def __init__(self, name, x=None, y=None):
        self.name = name
        self.x = x
        self.y = y
        self.val = None
        self.prompt_init()

    def prompt_init(self):
        val = input(self.name + ': ')
        self.val = val

    def __repr__(self):
        if self.val:
            return ': '.join([self.name, self.val])
        else:
            return self.name


if __name__ == '__main__':
    shipment = Shipment()
    movement = Movement(shipment)
    movement.determine_move_mode()
