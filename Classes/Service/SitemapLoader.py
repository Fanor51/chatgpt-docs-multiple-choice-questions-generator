#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import json

class SitemapLoader:
    def __init__(self, jsonPath):
        self.jsonPath = jsonPath
    
    def load_sitemap(self):
        with open(self.jsonPath) as file:
            return json.load(file)