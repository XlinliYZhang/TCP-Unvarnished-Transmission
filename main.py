import socketserver
TCP_Host = "127.0.0.1"
TCP_Port = 6666
tcp_list = []


# 服务器转发
class MySockServer(socketserver.BaseRequestHandler):  # 定义一个类
    def handle(self):
        # 打印连接的客户端地址
        print("[Connection]", self.client_address)
        tcp_list.append(self)
        while True:
            # 尝试接收数据
            data = self.request.recv(1024)
            # 如果数据为0 则连接断开
            if not len(data):
                print("[Close]", self.client_address)
                tcp_list.remove(self)
                break
            print("[Receive]", self.client_address, "<-", data)
            for client in tcp_list:
                if client != self:
                    print("[Send]", client.client_address, "->", data)
                    client.request.sendall(data)


# 服务器启动
def server_start():
    print("[Start]")
    # 创建Socket
    s = socketserver.ThreadingTCPServer((TCP_Host, TCP_Port), MySockServer)
    # 调用SocketServer模块的多线程并发函数
    s.serve_forever()


# 服务器停止
def server_stop():
    print("[Stop]")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    server_start()
