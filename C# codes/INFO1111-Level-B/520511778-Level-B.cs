namespace Attempt_3;
class Wizard
{
    public string name;
    public string favSpell;
    public int spellSlots;
    public float exp;
    public float health;
    public int attackDamage;

    public static int Count;

    public Wizard(string _name, string _favSpell)
    {
        name = _name;
        favSpell = _favSpell;
        spellSlots = 2;
        exp = 0f;
        health = 10f;
        attackDamage = 1;

        Count++;
    }
    
    public void CastSpell(Wizard target)
    {
        // using an attack will increase xp by 0.25 and decrease the other wizard by the attack damage
        if (spellSlots > 0) {
            Console.WriteLine(favSpell + " does " + attackDamage + " damage");
            Console.WriteLine(name + " casts " + favSpell);
            spellSlots--;
            exp += 0.25f;
            attackDamage = (Convert.ToInt32(exp) + 1);
            target.health -= attackDamage;

        } else {
            Console.WriteLine(name + " is out of spell slots.");
        }
        
    }

    public void Meditate()
    {
        // meditating will icnrease the wizards xp by 0.5 and their health by 1
        Console.WriteLine(name + " meditates to regain spell slots.");
        exp += 0.5f;
        spellSlots++;
        health += 1;
    }

    public void Flee()
    {
        // choosing to flee will end the game
        Console.WriteLine(name + " has chosen to flee!");
    }
}

class Program
{
    public static void Main(string[] args)
    {
        Console.ForegroundColor = ConsoleColor.Cyan;

        // Asking for names and favourite spells
        Console.Write("What is your name wizard? ");
        string wizName01 = Console.ReadLine();
        Console.Write("What is your wizards favourite spell " + wizName01 + "? ");
        string wizSpell01 = Console.ReadLine();
        Console.WriteLine("Excellent choice " + wizName01 + ", the " + wizSpell01 + " spell is extremely powerful!");

        Console.Write("Oh your fierce rival has arrived, what is your name challenger? ");
        string wizName02 = Console.ReadLine();
        Console.Write("And what the spell you will challenge " + wizName01 + " with " + wizName02 + "? ");
        string wizSpell02 = Console.ReadLine();
        Console.WriteLine("Excellent choice " + wizName02 + ", the " + wizSpell02 + " spell is nasty counterspell to " + wizSpell01 + "!");

        // Defining wizard 1 and wizard 2
        Wizard wizard01 = new Wizard(wizName01, wizSpell01);

        Wizard wizard02 = new Wizard(wizName02, wizSpell02);

        // Asking if the two wizards want to fight
        Console.Write(wizard01.name + " would you like to engage " + wizard02.name + " in combat, yes or no? ");
        string combatWiz01 = Console.ReadLine();
        if (combatWiz01 == "yes") {
            Console.WriteLine(wizard02.name + " now is your final chance to walk away. Do you wish to engage with " + wizard01.name + ", yes or no.");
            string combatWiz02 = Console.ReadLine();
            if (combatWiz02 == "yes") {
                Console.WriteLine("Ahhh, this should be interesting. DRAW! YOUR! WANDS!!!");
            } else {
                Console.WriteLine("Wise choice " + wizard02.name + ", " + wizard01.name + " has a very powerful energy that I can sense.");
                Environment.Exit(0);
            }
        } else {
            Console.WriteLine("Wise choice " + wizard01.name + ", " + wizard02.name + " has a very powerful energy that I can sense.");
            Environment.Exit(0);
        }

        Console.WriteLine(wizard01.name + " since you were here first, you will start.");

        while (true) 
        {
            // Wizard one's turn
            Console.WriteLine(wizard01.name + "'s turn:");
            Console.WriteLine("Enter 1 to attack, 2 to meditate or 3 to flee:");
            int choice01 = Convert.ToInt32((Console.ReadLine()));

            if (choice01 == 1) {
                wizard01.CastSpell(wizard02);
                Console.WriteLine(wizard01.name + " has " + wizard01.spellSlots + " spell slots left, " + wizard01.exp + " experience and " + wizard01.health + " health left.");
                Console.WriteLine(wizard02.name + " has " + wizard02.spellSlots + " spell slots left, " + wizard02.exp + " experience and " + wizard02.health + " health left.");
            } else if (choice01 == 2) {
                wizard01.Meditate();
                Console.WriteLine(wizard01.name + " has " + wizard01.spellSlots + " spell slots left, " + wizard01.exp + " experience and " + wizard01.health + " health left.");
            } else if (choice01 == 3) {
                wizard01.Flee();
                Console.WriteLine(wizard02.name + " wins!");
                Environment.Exit(0);
            } else {
                Console.WriteLine("You have picked neither, you have forfited your turn.");
            }

            if (wizard02.health <= 0) {
                Console.WriteLine(wizard01.name + " wins!");
                Environment.Exit(0);
            }
            
            Console.WriteLine("\n");

            // Wizard two's turn
            Console.WriteLine(wizard02.name + "'s turn:");
            Console.WriteLine("Enter 1 to attack, 2 to meditate or 3 to flee:");
            int choice02 = Convert.ToInt32((Console.ReadLine()));

            if (choice02 == 1) {
                wizard02.CastSpell(wizard01);
                Console.WriteLine(wizard02.name + " has " + wizard02.spellSlots + " spell slots left, " + wizard02.exp + " experience and " + wizard02.health + " health left.");
                Console.WriteLine(wizard02.name + " has " + wizard01.spellSlots + " spell slots left, " + wizard01.exp + " experience and " + wizard01.health + " health left.");
            } else if (choice02 == 2) {
                wizard02.Meditate();
                Console.WriteLine(wizard02.name + " has " + wizard02.spellSlots + " spell slots left, " + wizard02.exp + " experience and " + wizard02.health + " health left.");
            } else if (choice02 == 3) {
                wizard02.Flee();
                Console.WriteLine(wizard01.name + " wins!");
                Environment.Exit(0);
            } else {
                Console.WriteLine("You have picked neither, you have forfited your turn.");
            }

            if (wizard01.health <= 0) {
                Console.WriteLine(wizard02.name + " wins!");
                Environment.Exit(0);
            }

            Console.WriteLine("\n");
        }

        Console.ReadKey();
    }
}