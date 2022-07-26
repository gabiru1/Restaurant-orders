class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
            self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append({
            'cliente': customer,
            'pedido': order,
            'dia': day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        foods = {}
        info_cliente = [
            info for info in self.data if info['cliente'] == customer
            ]

        for info in info_cliente:
            if info['pedido'] not in foods:
                foods[info['pedido']] = 1
            else:
                foods[info['pedido']] += 1

        return max(foods, key=foods.get)


    def get_never_ordered_per_customer(self, customer):
        menus = set()
        custumer_orders = set()

        for info in self.data:
            if info['cliente'] == customer:
                custumer_orders.add(info['pedido'])
            menus.add(info['pedido'])
        never_ordered = menus.difference(custumer_orders)

        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        custumer_days = set()
        days = set()

        for info in self.data:
            if info['cliente'] == customer:
                custumer_days.add(info['dia'])
            days.add(info['dia'])
        days_never_visited = days.difference(custumer_days)

        return days_never_visited

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
