from datetime import datetime

request = bytes.fromhex("20 c7 00 00 00 06 01 03 00 00 00 04")
response = bytes.fromhex("20 c7 00 00 00 0b 01 03 08 02 89 01 62 04 95 00 00")

print("ACICP302 Activity 03: Manual Modbus/TCP Decode")
print("Analysis time:", datetime.now().astimezone().isoformat())
print("Source: previously captured Wireshark bytes")
print("\nREQUEST")
print("Raw bytes:", request.hex(" "))
print("Transaction ID:", hex(int.from_bytes(request[0:2], "big")))
print("Protocol ID:", int.from_bytes(request[2:4], "big"))
print("Length:", int.from_bytes(request[4:6], "big"))
print("Unit ID:", request[6])
print("Function code:", f"0x{request[7]:02X}")
print("Starting register address:", int.from_bytes(request[8:10], "big"))
quantity = int.from_bytes(request[10:12], "big")
print("Register quantity:", quantity)

print("\nRESPONSE")
print("Raw bytes:", response.hex(" "))
print("Transaction ID:", hex(int.from_bytes(response[0:2], "big")))
print("Protocol ID:", int.from_bytes(response[2:4], "big"))
print("Length:", int.from_bytes(response[4:6], "big"))
print("Unit ID:", response[6])
print("Function code:", f"0x{response[7]:02X}")
byte_count = response[8]
print("Data byte count:", byte_count)
data = response[9:9 + byte_count]
registers = [
    int.from_bytes(data[i:i+2], "big")
    for i in range(0, len(data), 2)
]
print("Register values:", registers)

print("\nREGISTER INTERPRETATION")
if len(registers) == 4:
    print(f"Register 0: {registers[0]} = {registers[0]/10:.1f} °C")
    print(f"Register 1: {registers[1]} = {registers[1]/10:.1f} bar")
    print(f"Register 2: {registers[2]} = {registers[2]/10:.1f} Nm³/h")
    print(f"Register 3: {registers[3]} = alarm {'inactive' if registers[3] == 0 else 'active'}")

print("\nVALIDATION")
print("Transaction IDs match:",
      request[0:2] == response[0:2])
print("Function codes match:",
      request[7] == response[7] == 3)
print("Request asks for four registers:", quantity == 4)
print("Response contains four registers:", len(registers) == 4)
print("\nNOTE: This is offline decoding of supplied bytes.")
print("It does not independently verify packet endpoints or timestamps.")
