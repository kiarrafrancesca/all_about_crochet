def stitches_menu():
    while True:
        try:
            print("<----------------------------------->")
            print("|     STITCH LEARNING ASSISTANT     |")
            print("<----------------------------------->")
            print("| [1] Basic                         |")
            print("| [2] Intermediate                  |")
            print("| [3] Advanced                      |")
            print("<----------------------------------->")
            print("| [4] Return to main menu           |")
            print("<----------------------------------->")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                basic()
            elif choice == 2:
                intermediate()
            elif choice == 3:
                advanced()
            elif choice == 4:
                print("Returning to main menu...")
                return
            else:
                print("Please enter a valid choice from the menu.")
        
        except ValueError:
            print("Please enter a valid choice from the menu.")

def basic():
    print("<--------------------------------------------------------------------------------------------------------------->")
    print("|                                            BASIC CROCHET STITCHES                                             |")
    print("<--------------------------------------------------------------------------------------------------------------->")
    print("| Chain Stitch (ch)                                                                                             |")
    print("| - The foundation of most crochet projects, this is the starting stitch used to create a base chain.           |")
    print("|\n Slip Stitch (sl st)                                                                                         |")
    print("| - A simple stitch used to join work, create a smooth edge, or move the yarn to a different position without   |")
    print("|   adding height.                                                                                              |")
    print("|\n Single Crochet (sc)                                                                                         |")
    print("| - It's one of the shortest stitches in crochet.                                                               |")
    print("| - A basic stitch that creates a dense, firm fabric.                                                           |")
    print("|\n Half Double Crochet (hdc)                                                                                   |")
    print("| - A stitch that's taller than a single crochet but shorter than a double crochet.                             |")
    print("| - It creates a slightly more open fabric.                                                                     |")
    print("|\n Double Crochet (dc)                                                                                         |")
    print("| - A common stitch that creates a looser, more flexible fabric than single crochet.                            |")
    print("|\n Treble/Triple Crochet (tr)                                                                                  |")
    print("| - A taller stitch than the double crochet, creating an even more open and airly fabric.                       |")
    print("<--------------------------------------------------------------------------------------------------------------->")

def intermediate():
    print("<--------------------------------------------------------------------------------------------------------------->")
    print("|                                       INTERMEDIATE CROCHET STITCHES                                           |")
    print("<--------------------------------------------------------------------------------------------------------------->")
    print("| Double Treble Crochet (dtr)                                                                                   |")
    print("| - An even taller stitch than the treble crochet, used to create very open and airy fabrics.                   |")
    print("|\n Front Post Double Crochet (fpdc)                                                                            |")
    print("| - A stitch worked around the post of the stitch in the previous row, rather than through the top loops.       |")
    print("|\n Back Post Double Crochet (bpdc)                                                                             |")
    print("| - Similar to the front post double crochet, but worked around the back of the post, creating a recessed       |")
    print("|   texture.                                                                                                    |")
    print("|\n Shell Stitch                                                                                                |")
    print("| - A decorative stitch where multiple stitches (usually double crochets) are worked into the same stitch or    |")
    print("| - space, creating a shell-like shape.                                                                         |")
    print("|\n V-Stitch                                                                                                    |")
    print("| - A pattern where two stitches (usually double crochets) are worked into the same space, separated by a chain |")
    print("|   stitch, forming a V shape.                                                                                  |")
    print("<--------------------------------------------------------------------------------------------------------------->")

def advanced():
    print("<--------------------------------------------------------------------------------------------------------------->")
    print("|                                         ADVANCED CROCHET STITCHES                                             |")
    print("<--------------------------------------------------------------------------------------------------------------->")
    print("| Puff Stitch                                                                                                   |")
    print("| - A cluster of half-completed stitches gathered together to create a puffy, textured effect.                  |")
    print("|\n Bobble Stitch                                                                                               |")
    print("| - A group of stitches worked together in the same stitch to create a raised, rounded bump on the fabric.      |")
    print("|\n Popcorn Stitch                                                                                              |")
    print("| - Similar to the bobble stitch but typically has more height, creating a more pronounced, rounded shape.      |")
    print("|\n Basket Weave Stitch                                                                                         |")
    print("| - Is achieved by alternating groups of front post and back post double crochets, forming raised and recessed  |")
    print("|   blocks that mimic a weave.                                                                                  |")
    print("|\n Alpine Stitch                                                                                               |")
    print("| - Is a highly textured stitch that combines front post double crochets and regular double crochets to create  |")
    print("|   a raised, zigzag pattern.                                                                                   |")
    print("<--------------------------------------------------------------------------------------------------------------->")