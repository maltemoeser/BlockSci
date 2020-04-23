def address_types(chain_name):
    if chain_name == "btc":
        return ["p2sh", "p2wsh"]
    else:
        return ["p2sh"]


def addresses(chain, json_data, chain_name):
    for addr_type in address_types(chain_name):
        for i in range(3):
            addr = chain.address_from_string(
                json_data["address-{}-spend-{}".format(addr_type, i)]
            )
            yield addr, addr_type


def sort_addresses(lst):
    return sorted(lst, key=lambda a: a.address_string)


def test_script_equivalence(chain, json_data, regtest, chain_name):
    for addr, addr_type in addresses(chain, json_data, chain_name):

        script_equiv = sort_addresses(addr.equiv(True).addresses.to_list())
        for equiv_address in script_equiv:
            assert script_equiv == sort_addresses(equiv_address.equiv(True).addresses.to_list())


def test_type_equivalence(chain, json_data, regtest, chain_name):
    pass
