# Jacqueline Kory Westlund
# May 2016
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Personal Robots Group
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class jibo_teleop_flags:

    # is jibo currently playing audio?
    # we get this info from the jibo state rosmsgs
    _jibo_is_playing_sound = False
    @property
    def jibo_is_playing_sound(self):
        return self._jibo_is_playing_sound
    @jibo_is_playing_sound.setter
    def jibo_is_playing_sound(self,val):
        self._jibo_is_playing_sound = val

    # is jibo currently doing a motion?
    # we get this info from the jibo state rosmsgs
    _jibo_is_doing_motion = False
    @property
    def jibo_is_doing_motion(self):
        return self._jibo_is_doing_motion
    @jibo_is_doing_motion.setter
    def jibo_is_doing_motion(self,val):
        self._jibo_is_doing_motion = val

    # is jibo currently listening
    # we get this info from the jibo state rosmsgs
    _jibo_is_listening = False
    @property
    def jibo_is_listening(self):
        return self._jibo_is_listening
    @jibo_is_listening.setter
    def jibo_is_listening(self,val):
        self._jibo_is_listening = val

