#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
  """
  Triangle analyzes the lengths of the sides of a triangle
  (represented by a, b and c) and returns the type of triangle.

  It returns:
    'equilateral'  if all sides are equal
    'isosceles'    if exactly 2 sides are equal
    'scalene'      if no sides are equal
  """
  triangle_types = {1: 'equilateral', 2: 'isosceles', 3: 'scalene'}
  sides = sorted((a, b, c))

  if sides[0] <= 0 or (sides[0] + sides[1]) <= sides[2]:
      raise TriangleError('illegal triangle')

  return triangle_types[set(sides).__len__()]

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
