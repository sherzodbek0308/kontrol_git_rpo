def show_project_title():
    print("Контрольная работа: Git, GitHub и VS Code")


def show_git_actions():
    actions = [
        "Clone Repository",
        "Initialize Repository",
        "Stage Changes",
        "Commit",
        "Publish Branch",
        "Push / Sync Changes",
        "Fetch",
        "Pull",
        "Create Branch",
        "Merge",
    ]

    print("Git-действия для выполнения:")
    for number, action in enumerate(actions, start=1):
        print(f"{number}. {action}")


def main():
    show_project_title()
    print()
    show_git_actions()


if __name__ == "__main__":
    main()

