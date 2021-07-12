from fpdf import FPDF
import pandas as pd

class Random:

    def __init__(self, itemz):
        self.itemz = itemz

    # Build list of items
    def build_list(self):
        self.itemz = (input("Please enter the items you wish to shuffle: (separate items with commas, no space) "
                            ).split(','))
        # Print number of items entered
        count = len(self.itemz)
        print("\n --> ", count, " Items!")
        print(*self.itemz, sep=', ')
        # Ask if anymore need to be added, if Y enter and append. If no shuffle the list and print.
        another = 'Y'
        while another == 'Y':
            another = input("\n Enter another item? \n (Y/N) MUST BE CAPS ").upper()
            if another == "Y":
                itemz2 = (
                    input("Please enter the items you wish to shuffle: (separate items with commas, no space) ").split(
                        ','))
                for x in itemz2:
                    self.itemz.append(x)
                    count = len(self.itemz)
                    print("\n --> ", count, " Items!")
                    print(*self.itemz, sep=', ')
            else:
                print('\n')
                self.list_shuffle()
                self.print_shuffle()
                self.doagain()
    # shuffle the original list of items
    def list_shuffle(self):
        import random
        rand_itemzs = self.itemz.copy()
        y = 0
        for x in self.itemz:
            if x == rand_itemzs[y]:
                random.shuffle(rand_itemzs)
            y = y + 1
        return rand_itemzs
    # print the original list beside the shuffled list
    def print_shuffle(self):
        table = {}
        shuff_list = self.list_shuffle()
        count = len(self.itemz) + 1
        index = range(1, count)
        table['Items'] = self.itemz
        table['Shuffled'] = shuff_list
        df = pd.DataFrame(data=table, index=index, )
        print (df)
    # ask if you would like to shuffle the list again. If yes, shuffle and ask if you would like to shuffle again.
    # if no, ask to save the list to .pdf
    def doagain(self):
        print("Would you like to shuffle again? \n")
        again = input("Y/N " + "(ALL CAPS)? ").upper()
        if again != 'N':
            print('\n')
            self.print_shuffle()
            self.doagain()
        else:
            print('\n')
            myprint = input("Save your list to .pdf for file/print? Y/N  ").upper()
            if myprint == 'Y':
                pdf = FPDF('L', 'in', 'Letter')
                pdf.add_page()
                pdf.set_font('Times', '', 16)
                pdf.write(10)
                pdf.output('myrandomlist.pdf', 'F').encode('latin-1')

            pass


runit = Random('')
runit.build_list()
