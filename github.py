import requests
import sys

def get_org_members(org_name):
    """
    Fetches the list of members in a GitHub organization using Tor proxy.

    Args:
        org_name (str): The name of the GitHub organization.

    Returns:
        list: A list of GitHub usernames of the organization's members.
    """
    url = f"https://api.github.com/orgs/{org_name}/members"
    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }

    members = []
    page = 1

    while True:
        try:
            response = requests.get(url, params={"page": page, "per_page": 100}, proxies=proxies)
            if response.status_code != 200:
                print(f"Failed to fetch members: {response.status_code} - {response.text}")
                sys.exit(1)

            data = response.json()
            if not data:
                break

            members.extend(member["login"] for member in data)
            page += 1

        except requests.exceptions.RequestException as e:
            print(f"Error fetching members: {e}")
            sys.exit(1)

    return members

def save_members_to_file(org_name, members):
    """
    Saves the list of members to a text file.

    Args:
        org_name (str): The name of the GitHub organization.
        members (list): The list of GitHub usernames.
    """
    filename = f"{org_name}_members.txt"
    with open(filename, "w") as f:
        f.write("\n".join(members))
    print(f"Saved {len(members)} members to {filename}")

def main():
    print("\n=== GitHub Organization Member Fetcher ===")
    org_name = input("Enter the GitHub organization name: ").strip()

    if not org_name:
        print("Organization name cannot be empty.")
        sys.exit(1)

    print("Fetching members, please wait...")
    members = get_org_members(org_name)

    if members:
        print(f"Fetched {len(members)} members successfully!")
        save_members_to_file(org_name, members)
    else:
        print("No members found or failed to fetch members.")

if __name__ == "__main__":
    main()
