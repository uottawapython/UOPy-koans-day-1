#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutOperators(Koan):

    def test_assignment_operator(self):
        """
        Assume this variable holds a value
        """
        my_var = 5
        self.assertEqual(__, my_var)

    def test_multiple_assignments(self):
        """
        parallel assignments
        """
        a, b, c = 5, 6, 8
        self.assertEqual(__, b)

    def test_arithmetics_operators(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(__, 1 * 5)
        self.assertEqual(__, 2 ** 2)

        self.assertEqual(__, 4 / 2)
        self.assertEqual(__, 7 // 4)

        self.assertEqual(__, 13 / 4)
        self.assertEqual(__, 13 % 4)

    def test_increment_operator(self):
        """
        those are operator assignments also

        It adds right operand to the left operand
        and assign the result to left operand.
        """
        a = 5
        self.assertEqual(__, a)

        a += 1
        self.assertEqual(__, a)

        a = 5
        a -= 1
        self.assertEqual(__, a)

        a = 5
        a *= 2
        self.assertEqual(__, a)

        a = 8
        a /= 2
        self.assertEqual(__, a)

        a = 7
        a %= 2
        self.assertEqual(__, a)


    def test_comparaison_operators(self):
        """
        These operators compare the values on either sides
        of them and decide the relation among them.

        Comparaison operator always return a Boolean (True/False)
        """
        #change the value of the variable 'number'
        number = 53
        self.assertTrue(number == __)

        #change the value of the variable number
        number = 3
        self.assertTrue(number != __)

        #change the value of the variable number
        number = 53
        self.assertTrue(number < __)

        #change the value of the variable number
        number = 53
        self.assertTrue(number <= __)

        #change the value of the variable number
        number = 2
        self.assertTrue(number >= __)

        #change the value of the variable number
        number = 2
        self.assertTrue(number > __)


    def test_membership_operators(self):
        """
        Python’s membership operators test for membership
         in a sequence, such as strings, lists, or tuples.

        Membership operators always return a Boolean (True/False)
        """
        #change the value of the variable university
        university = 'Morisset'
        self.assertTrue('e' in university )

        #change the value of the variable greeting
        greeting = 'hello world'
        self.assertTrue('e' not in greeting)

    def test_identity_operators(self):
        """
        Identity operators compare the memory locations of two objects

        Identity operators always return a Boolean (True/False)
        """

        #change the value of the variable 'director'
        director = False
        self.assertTrue(director is True)

        #change the value of the variable 'my_program'
        course = "Geography"

        my_program = __
        self.assertTrue(my_program is course)

    def test_priority_of_operators(self):
        """
        Test operator precedence
        """
        #change the value of the variable 'athlete'
        athlete = False
        self.assertTrue(athlete is __)


        statement = False is False is False
        #replace 0 by the value of the variable 'statement'
        self.assertTrue(__)

        statement_2 = (False is False) is False
        #replace 1 by the value of the variable 'statement'
        self.assertFalse(__)
