#!/usr/bin/env python
# encoding: utf-8


class PlayerMiddleware(object):

    def process_request(self, request):
        user = request.user
        if not user.is_anonymous():
            request.player = request.user.player
