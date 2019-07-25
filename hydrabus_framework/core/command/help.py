def hbf_help(hbf_instance):
    """
    Print framework help on the console
    """
    print()
    print("Core Commands")
    print("=============")
    formatted_commands = []
    for cmd in hbf_instance.command:
        formatted_commands.append(
            {
                "Command": cmd["name"],
                "Description": cmd["descr"]
            }
        )
    hbf_instance.logger.print_tabulate(formatted_commands, headers={"name": "Name", "descr": "Description"})