#!/usr/bin/python3

# Copyright (C) 2011-2020 Jeff Epler <jepler@gmail.com>
# SPDX-FileCopyrightText: 2021 Jeff Epler
#
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
import wwvbgen
import os


class TestPhaseModulation(unittest.TestCase):
    def test_pm(self):

        ref_am = (
            "2011000002"
            "0001001112"
            "0001010002"
            "0110001012"
            "0100000012"
            "0010010112"
        )

        ref_pm = (
            "0011101101"
            "0001001000"
            "0011001000"
            "0110001101"
            "0011010001"
            "0110110110"
        )

        ref_minute = wwvbgen.WWVBMinuteIERS(2012, 186, 17, 30, dst=3)
        ref_time = ref_minute.as_timecode()

        test_am = ref_time.to_am_string("012")
        test_pm = ref_time.to_pm_string("01")

        self.assertEqual(ref_am, test_am)
        self.assertEqual(ref_pm, test_pm)


if __name__ == "__main__":
    unittest.main()
