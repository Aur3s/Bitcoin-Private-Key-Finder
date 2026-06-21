
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=header&text=✨%20Made%20with%20Magic%20✨&fontSize=40&fontAlignY=35&descAlignY=51&descAlign=62&animation=twinkling" width="100%"/>
</p>

<p align="center">
  <img src="https://i.ytimg.com/vi/ILWJQ73iXg0/maxresdefault.jpg" alt="Bitcoin Private Key Recovery Tool">
</p>


# Bitcoin Private Key Recovery Tool

A Bitcoin private key recovery utility designed for situations where a portion of a private key is already known but some characters are missing.

The tool performs a targeted search by generating candidate keys from the known pattern, deriving their corresponding Bitcoin addresses, and comparing them against a specified target address. When a match is found, the correct private key is identified.

> This project is intended for legitimate recovery scenarios where the owner possesses partial knowledge of the original private key.

---

## Features

* Recover partially known Bitcoin private keys
* Flexible wildcard-based search
* Offline recovery process
* Optional Discord notifications
* Terminal-friendly output
* Compatible with Linux, Windows, and Termux

---

## Recovery Model

Unknown characters within the private key must be replaced with:

```text
?
```

Example:

```text
KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU73sVHn???
```

The software systematically generates candidate combinations for the unknown positions and verifies each result by deriving the corresponding Bitcoin address.

---

## Requirements

* Python 3.10+
* Internet connection only if Discord notifications are enabled

---

## Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Install dependencies:

```bash
pip install requests
pip install bitcoin
pip install colorama
```

---

## Usage

Run the application:

```bash
python main.py
```

Provide:

* The target Bitcoin address
* The partially known private key
* Missing positions marked using `?`

The recovery process will begin immediately.

---

## Discord Notifications (Optional)

The tool can send a Discord notification when a matching private key is discovered.

Locate the webhook configuration inside the source code and replace:

```text
DISCORD WEBHOOKS
```

with your Discord webhook URL.

---

## Performance Considerations

Recovery speed depends primarily on:

* Number of unknown characters
* Available CPU resources
* Search space size

As the number of missing characters increases, the number of combinations grows exponentially. Small recovery jobs may complete quickly, while larger searches can require significant computational time.

Example:

| Missing Characters | Difficulty |
| ------------------ | ---------- |
| 1–4                | Low        |
| 5–8                | Moderate   |
| 9–12               | High       |
| 13+                | Very High  |

Actual recovery times vary depending on hardware and key structure.

---

## Security

All key generation and verification operations are performed locally.

No recovery data is transmitted externally.

If Discord notifications are enabled, only the notification message is sent through the configured webhook.

---

## Platform Support

Tested on:

* Windows
* Linux
* Termux (Android)

---

## Disclaimer

This software is provided for educational and legitimate wallet recovery purposes only.

The author assumes no responsibility for misuse, data loss, financial loss, or improper operation of the software.

Use at your own risk.

---

## Demonstration

Video walkthrough:

https://www.youtube.com/watch?v=ILWJQ73iXg0&t=335s

---

## License

See the LICENSE file for licensing information.

<p align="center">
  <a href="https://github.com/Aur3s/Bitcoin-Private-Key-Finder">
    <img src="https://komarev.com/ghpvc/?username=Aur3s&repo=Bitcoin-Private-Key-Finder&style=flat-square" alt="Visitors">
  </a>
</p>
