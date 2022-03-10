class Birds:
    def fly(self):
        print("All birds can fly")
class Pigeon(Birds):
    def fly(self):
        super().fly()
        print("Pigeon can fly")
ab = Pigeon()
ab.fly()
