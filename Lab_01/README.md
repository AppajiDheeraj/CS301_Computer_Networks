# Lab 01: Basic LAN using Router, Switch and Hub

## Question

Configure a small office LAN using one router, one switch, one hub, PCs, and a printer. Use static IP addressing, configure the router interface and default gateway, verify connectivity using ping, observe ARP packets in Simulation Mode, and compare switch and hub behavior.

## Objective

Build a basic LAN in Cisco Packet Tracer and understand how end devices communicate through a switch, hub, and router using static IP addresses.

## Topology

Use the topology from the Week 2 resource:

![Lab 01 topology](resources/lab-01-topology.png)

For Lab 01, focus on the first diagram: **Basic LAN using Router, Switch and Hub**.

## Devices Required

| Device | Quantity | Suggested Packet Tracer Device |
| --- | ---: | --- |
| Router | 1 | Router 2911 or any router with `GigabitEthernet0/0` |
| Switch | 1 | 2960 switch |
| Hub | 1 | Hub-PT |
| PCs | 3 | PC-PT |
| Printer | 1 | Printer-PT |
| Copper straight-through cables | As needed | Connections between unlike devices |

## IP Addressing Table

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | `192.168.10.1` | `255.255.255.0` | Not required |
| PC1 | FastEthernet0 | `192.168.10.10` | `255.255.255.0` | `192.168.10.1` |
| PC2 | FastEthernet0 | `192.168.10.11` | `255.255.255.0` | `192.168.10.1` |
| PC3 | FastEthernet0 | `192.168.10.12` | `255.255.255.0` | `192.168.10.1` |
| Printer | FastEthernet0 | `192.168.10.13` | `255.255.255.0` | `192.168.10.1` |

## Connections

| From | To | Cable |
| --- | --- | --- |
| R1 G0/0 | SW1 port | Copper straight-through |
| PC1 Fa0 | SW1 port | Copper straight-through |
| PC2 Fa0 | SW1 port | Copper straight-through |
| Hub-PT port | SW1 port | Copper straight-through |
| PC3 Fa0 | Hub-PT port | Copper straight-through |
| Printer Fa0 | Hub-PT port | Copper straight-through |

## Router Configuration

Open R1 CLI and enter:

```text
enable
configure terminal
hostname R1
interface gigabitEthernet0/0
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
end
write memory
```

Verify the interface:

```text
show ip interface brief
```

Expected result: `GigabitEthernet0/0` should show IP `192.168.10.1` and status `up/up`.

## End Device Configuration

On each PC:

1. Open the device.
2. Go to **Desktop > IP Configuration**.
3. Select **Static**.
4. Enter the IP address, subnet mask, and default gateway from the table.

On the printer:

1. Open the printer.
2. Go to **Config > FastEthernet0** or **Desktop > IP Configuration** depending on Packet Tracer version.
3. Assign `192.168.10.13 / 255.255.255.0`.
4. Set gateway as `192.168.10.1`.

## Verification

From PC1 Command Prompt:

```text
ping 192.168.10.1
ping 192.168.10.11
ping 192.168.10.12
ping 192.168.10.13
```

Expected result: all pings should succeed. The first ping may timeout once because ARP needs to resolve the MAC address.

## Observe ARP in Simulation Mode

1. Switch Packet Tracer from **Realtime** to **Simulation**.
2. From PC1, ping PC2: `ping 192.168.10.11`.
3. Watch ARP packets before ICMP packets.
4. Click the packet envelope to inspect source and destination MAC/IP details.

Answer: ARP is used to discover the MAC address that belongs to a known IP address in the same LAN. After ARP resolves the MAC address, ICMP echo packets can be sent.

## Switch vs Hub Behavior

| Device | Behavior |
| --- | --- |
| Switch | Learns MAC addresses and forwards frames only to the correct port after learning. |
| Hub | Repeats incoming bits out of all other ports, so all connected devices receive the traffic. |

In Simulation Mode, traffic through the hub is visible to every device connected to the hub. Traffic through the switch becomes more targeted after the switch learns MAC addresses.

## Assignment Answers

### 1. What is the purpose of this lab?

To configure a small LAN with static IP addresses and verify communication between devices connected through a router, switch, and hub.

### 2. Why do we configure `192.168.10.1` on the router?

The router interface `192.168.10.1` acts as the default gateway for all hosts in the `192.168.10.0/24` network.

### 3. What is a default gateway?

A default gateway is the router IP address used by a host to send traffic outside its local network.

### 4. Can PC1 ping PC2 without the router?

Yes. PC1 and PC2 are in the same network, so they can communicate through the switch without needing the router.

### 5. Why is the router still configured?

The router provides the gateway for communication outside the LAN and completes the standard LAN design.

### 6. What is ARP?

ARP means Address Resolution Protocol. It maps an IPv4 address to a MAC address inside the local network.

### 7. Why can the first ping fail?

The first ping can fail because the sender may need time to perform ARP resolution before sending ICMP packets.

### 8. What is the difference between a switch and a hub?

A switch forwards frames based on MAC addresses. A hub simply repeats traffic to all connected ports.

### 9. Which device is more efficient: switch or hub?

A switch is more efficient because it reduces unnecessary traffic and separates collision domains.

### 10. What command verifies router interface status?

Use:

```text
show ip interface brief
```

### 11. What command saves router configuration?

Use:

```text
write memory
```

or:

```text
copy running-config startup-config
```

## Final Result

The lab is complete when:

- R1 G0/0 is configured as `192.168.10.1/24`.
- PC1, PC2, PC3, and Printer have static IP addresses.
- All hosts use `192.168.10.1` as default gateway.
- Ping works between all devices.
- ARP can be observed in Simulation Mode.
- Switch and hub traffic behavior can be compared.

## Submission Checklist

- Packet Tracer `.pkt` file saved in this folder.
- Screenshot of final topology.
- Screenshot of successful ping.
- Short written answers from this README.
