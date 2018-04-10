import maya.cmds as mc



class ListItems:                                #Define Class

    def __init__(self):                         # this is a function that represents the instance of the class itself
        self.win = mc.window(title="test", widthHeight=(300, 200))
        mc.columnLayout()
        self.listiter = mc.textScrollList( numberOfRows=8, allowMultiSelection=True,
			append=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
					'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen'],
			selectItem='six', showIndexedItem=4 )                                           #Here is a list of items that is being created in the UI

        mc.button(label = "print listItem", command = self.printList)                           # This is the "Print list item button at the bottom of the UI, see in the command it's calling
                                                                                                # the self.printList(this is the function that prints the item that is declared below)
        mc.showWindow(self.win)
    def printList(self, *args):                                                                 # This is the function in which you might do your maya operations, you should be able to query
                                                                                                # the selected item from the list here
        #self.selection.append(mc.ls(selection = True))
        item = mc.textScrollList(self.listiter, query = True, selectItem = True)                #Here is where we query the selected item from the list in the textScrollList we are loading the list
                                                                                                # we created in the previous function and querying it's selected item
        print "The selected item is" + str(item)



ListItems()