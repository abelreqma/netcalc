def ip_to_bin(ip):
   return ' '.join(format(int(octet), '08b') for octet in ip.split('.'))

def bin_to_ip(binip):
   octets = binip.split()
   if len(octets) != 4:
      raise ValueError("There must be at least 4 Octets")
   decocts = []
   for octet in octets:
      if not all(bit in '01' for bit in octet):
         raise ValueError("Binary only has 1s and 0s")
      if len(octet) > 8:
         raise ValueError("Each octet can be at most 8 bits long")
      decocts.append(str(int(octet.zfill(8), 2)))
   return '.'.join(decocts)

def valid_ip(ip):
   parts = ip.split('.')
   if len(parts) != 4:
      return False
   for part in parts:
      if not part.isdigit() or not 0 <= int(part) <= 255:
         return False
   return True

def valid_cidr(cidr):
   return cidr.isdigit() and 0 <= int(cidr) <= 32

def valid_subnet(subnet):
   parts = subnet.split('.')
   if len(parts) != 4:
      return False
   for part in parts:
      if not part.isdigit() or not 0 <= int(part) <= 255:
         return False
   return True

def to_cidr(subnet):
   return sum(bin(int(octet)).count('1') for octet in subnet.split('.'))

o = []

print("Welcome to NetCalc")
while True:
   response = input("1: Convert from Decimal\n2: Convert from Binary \n3: Quick Subnet \n4: Cancel \nSelection: ")
   if response == "1":
      ip = input("Input IPv4 Address (x.x.x.x): ")
      if not valid_ip(ip):
         print("Invalid IP address format")
         continue
      binip = ip_to_bin(ip)

      netmask = input("Input Subnet Mask (CIDR, Decimal, or No): ").lower()
      if netmask == 'cidr':
         subnet = input("Input Subnet Mask: ")
         if not valid_cidr(subnet):
            print("Invalid CIDR format")
            continue
         subnet = int(subnet)
         remainder = 32 - subnet
         print(f"Decimal: {ip}")
         print(f"Binary: {binip}")
         print(f"Subnet (binary): {'1' * subnet + '0' * remainder}")
         break

      elif netmask == 'decimal':
         subnet = input("Input Subnet Mask (x.x.x.x): ")
         if not valid_subnet(subnet):
            print("Invalid subnet mask format")
            continue
         binet = ip_to_bin(subnet)
         print(f"Decimal: {ip}")
         print(f"Binary: {binip}")
         print(f"Subnet (decimal): {binet}")
         break

      elif netmask == 'no':
         print(f"Decimal: {ip}")
         print(f"Binary: {binip}")
         break

      else:
         print("Please Type CIDR, Decimal, or No")

   elif response == "2":
      abel = input("Input Binary Address (separate octets with a space): ")
      try:
         maldoreq = bin_to_ip(abel)
         if not valid_ip(maldoreq):
            print("Invalid Binary IP Address Format")
            continue

         netmask = input("Input Subnet Mask (CIDR, Decimal, or No): ").lower()

         if netmask == 'cidr':
            subnet = input("Input Subnet Mask: ")
            if not valid_cidr(subnet):
               print("Invalid CIDR format")
               continue
            subnet = int(subnet)
            remainder = 32 - subnet
            print(f"Binary: {abel}")
            print(f"Decimal: {maldoreq}")
            print(f"Subnet (binary): {'1' * subnet + '0' * remainder}")
            break

         elif netmask == 'decimal':
            subnet = input("Input Subnet Mask (x.x.x.x): ")
            if not valid_subnet(subnet):
               print("Invalid subnet mask format")
               continue
            binet = ip_to_bin(subnet)
            print(f"Binary: {abel}")
            print(f"Decimal: {maldoreq}")
            print(f"Subnet (decimal): {binet}")
            break

         elif netmask == 'no':
            print(f"Binary: {abel}")
            print(f"Decimal: {maldoreq}")
            break

         else:
            print("Please Type CIDR, Decimal, or No")

      except ValueError as e:
         print(f"Error: {e}")

   elif response == "3":
      aic = input("Convert to CIDR (c) or Decimal (d)? ").lower()
      if aic == 'c':
         oasis = input("Input Subnet Mask (x.x.x.x): ")
         if not valid_subnet(oasis):
            print("Invalid subnet mask format")
            continue
         cidr = to_cidr(oasis)
         print(f"/{cidr} is {oasis} in CIDR Notation")
         break

      elif aic == 'd':
         foo = int(input("Input CIDR: "))
         if not valid_cidr(foo):
            print("Invalid CIDR format")
            continue
         bar = 32 - foo
         print(f"/{foo} in decimal notation is {'1' * foo + '0' * bar}")
         break
         
      else:
         print("Please type 'c' or 'd'")

   elif response == '4':
      break
   else:
      print("\nSelect a valid option")