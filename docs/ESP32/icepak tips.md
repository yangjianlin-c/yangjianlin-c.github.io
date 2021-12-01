---
title: Icepak Tips
date: 2014-11-18
tags: Icepak
categories: Thermal
---

This article will collect some useful Icepak tips.

<!-- more -->

# How to include solar loading in an Icepak model?

The solar loading can directly be modeled beginning in ANSYS Icepak. Here is the procedure:

1. Enable Solar Loading from Basic Parameters / General Advanced Setup
2. Specify Date, Month, Time and Location information ( Time input is based on a 24 hr clock)
3. Specify Illumination Parameters
 - Sunshine fraction: 0 to 1: Used to account for the effects of clouds which may reduce the direct solar irradiation.
 - Ground Reflectance: 0 to 1: Determines the contribution of reflected solar radiation from ground surfaces.
4.  Define the North direction vector. +X is default North