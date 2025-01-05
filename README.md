# GitHub Organization Member Fetcher

This Python script retrieves the usernames of all members in a specified GitHub organization using the GitHub API and Tor proxy to bypass rate limits.

## Prerequisites
1. **Python 3**: Ensure Python 3 is installed (`python3 --version`).
2. **Tor**: Install and start Tor:
   ```bash
   sudo apt install tor
   sudo service tor start
   ```
3. **Python Libraries**: Install required libraries:
   ```bash
   python3 -m pip install requests[socks]
   ```

## Usage
1. Save the script as `github_org_members.py`.
2. Run the script:
   ```bash
   python3 github_org_members.py
   ```
3. Enter the GitHub organization name when prompted.
4. The script saves the usernames to `<organization_name>_members.txt`.

## Example
For the organization `shopify`, the output will be saved in `shopify_members.txt`.

## Troubleshooting
- **Missing dependencies for SOCKS support**: Install `PySocks`:
  ```bash
  python3 -m pip install requests[socks]
  ```
- **Tor not running**: Start Tor:
  ```bash
  sudo service tor start
  ```

