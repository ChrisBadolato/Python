class atom:
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.position = (x,y,z)
    def symbol(self):
        return Anto_to_Symbol[atno]
    def __repr__(self):
        return  '%d%10.4f%10.4f%10.4f' % (self.atno, self.position[0], self.position[1], self.position[2])
    
class molecule:
    def __init__(self,name='Generic'):
        self.name = name
        self.atomlist = []
    def addatom(self,atom):
     self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule named %s\n' % self.name
        str = str+'It has %d atoms\n' % len(self.atomlist)
        for atom in self.atomlist:
         str = str + 'atom' + '\n'
        return str
