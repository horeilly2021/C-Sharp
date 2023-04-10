using System;

namespace attempt_2 // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {

            Console.ForegroundColor = ConsoleColor.Cyan;

            Console.WriteLine("Welcome to the calculator!");

            while (true) {

                Console.WriteLine("Press 1 to continue or 2 to quit: ");
                int welcome;

                if (!int.TryParse(Console.ReadLine(), out welcome)) {

                    Console.WriteLine("\r\nInvalid input, please enter a number.");
                    continue;

                }

                if (welcome == 1) {

                    while (true) {

                        Console.Write("\r\nPlease your first number: ");
                        double num01;

                        if (!double.TryParse(Console.ReadLine(), out num01)) {

                            Console.WriteLine("\r\nInvalid input, please enter a number.");
                            continue;

                        }

                        Console.Write("Please your second number: ");
                        double num02;

                        if (!double.TryParse(Console.ReadLine(), out num02)) {

                            Console.WriteLine("\r\nInvalid input, please enter a number.");
                            continue;
                            
                        }

                        Console.WriteLine("\r\nPlease enter what you would like to do:");
                        Console.Write("1. Add\r\n2. Subtract\r\n3. Multiply\r\n4. Divide\r\n5. Return to main\r\n");
                        int choice;

                        if (!int.TryParse(Console.ReadLine(), out choice)) {

                            Console.WriteLine("\r\nInvalid input, please enter a number.");
                            continue;

                        }

                        if (choice == 1) {

                            double added = num01 + num02;
                            Console.WriteLine("\r\nThe sum of " + num01 + " and " + num02 + " is " + added + "\r\n");
                            continue;

                        } else if (choice == 2) {

                            while (true) {

                                Console.WriteLine("\r\nFor the difference between " + num01 + " and " + num02 + " type 1.");
                                Console.WriteLine("For the difference between " + num02 + " and " + num01 + " type 2.");
                                int sub_choice;

                                if (!int.TryParse(Console.ReadLine(), out sub_choice)) {

                                    Console.WriteLine("\r\nInvalid input, please enter a number.");
                                    continue;

                                }

                                if (sub_choice == 1) {

                                    double subtract01 = num01 - num02;
                                    Console.WriteLine("\r\nThe difference between " + num01 + " and " + num02 + " is: " + subtract01);
                                    break;

                                } else if (sub_choice == 2) {

                                    double subtract02 = num02 - num01;
                                    Console.WriteLine("\r\nThe difference between " + num02 + " and " + num01 + " is: " + subtract02);
                                    break;

                                } else {

                                    Console.WriteLine("\r\nInvalid command, try again.");

                                }
                            }
                            continue;

                        } else if (choice == 3) {

                            double multiply = num01 * num02;
                            Console.WriteLine("\r\nThe product of " + num01 + " and " + num02 + " is " + multiply);
                            continue;

                        } else if (choice == 4) {

                            while (true) {

                                Console.WriteLine("\r\nFor the quotient between " + num01 + " and " + num02 + " type 1.");
                                Console.WriteLine("For the quotient between " + num02 + " and " + num01 + " type 2.");
                                int div_choice;

                                if (!int.TryParse(Console.ReadLine(), out div_choice)) {

                                    Console.WriteLine("\r\nInvalid input, please enter a number.");
                                    continue;

                                }

                                if (div_choice == 1) {

                                    double quotient01 = num01 / num02;
                                    Console.WriteLine("The quotient between " + num01 + " and " + num02 + " is: " + quotient01 + "\r\n");
                                    break;

                                } else if (div_choice == 2) {

                                    double quotient02 = num02 / num01;
                                    Console.WriteLine("The quotient between " + num02 + " and " + num01 + " is: " + quotient02 + "\r\n");
                                    break;

                                } else {

                                    Console.WriteLine("Invalid command, try again.");

                                }
                            }
                            continue;

                        } else if (choice == 5) {

                            Console.WriteLine("Returning to main\r\n");
                            break;

                        } else {
                            
                            Console.WriteLine("Invalid command, try again.");

                        }

                    }

                } else if (welcome == 2) {

                    Console.WriteLine("Thank you for using the calculator, Goodbye!");
                    Environment.Exit(0);

                } else {

                    Console.WriteLine("Invalid input, try again");

                }

            }

        }

    }

}