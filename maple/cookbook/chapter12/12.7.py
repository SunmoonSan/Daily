#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2019/12/21 11:50 上午
# @site  : https://github.com/SunmoonSan
from concurrent.futures.thread import ThreadPoolExecutor
from socket import socket, SOCK_STREAM, AF_INET


def echo_client(sock, client_addr):
    """
    Handle a client connection
    :param sock:
    :param client_addr:
    :return:
    """
    print("Got connection from", client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection")
    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


echo_server(('', 15000))
