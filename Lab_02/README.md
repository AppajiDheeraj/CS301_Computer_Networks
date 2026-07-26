# Lab 02: VLAN and Inter-VLAN Routing

## Question

Configure VLANs and Router-on-a-Stick inter-VLAN routing.

## Objective

Create separate VLANs for Admin, Faculty, and Students, configure a trunk link to the router, create router subinterfaces, verify inter-VLAN routing, and apply an ACL to block Students from Admin.

## VLAN Plan

| VLAN | Name | Network | Gateway |
| --- | --- | --- | --- |
| 10 | Admin | `192.168.10.0/24` | `192.168.10.1` |
| 20 | Faculty | `192.168.20.0/24` | `192.168.20.1` |
| 30 | Students | `192.168.30.0/24` | `192.168.30.1` |

## Main Tasks

1. Create VLAN 10, VLAN 20, and VLAN 30 on SW1.
2. Assign switch access ports to the correct VLANs.
3. Configure the router-facing switch port as an 802.1Q trunk.
4. Configure router subinterfaces for VLAN 10, 20, and 30.
5. Verify inter-VLAN communication with ping.
6. Configure an ACL to block Students from Admin if required.

