import smtplib
from email.mime.text import MIMEText
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def generate_quantum_otp() -> str:
    # ... same code as before ...
    circ = QuantumCircuit(1, 1)
    circ.h(0)
    circ.measure(0, 0)

    simulator = AerSimulator()
    circ = transpile(circ, simulator)
    result = simulator.run(circ, shots=20, memory=True).result()
    memory = result.get_memory(circ)

    random_binary_string = ''.join(memory)
    random_integer = int(random_binary_string, 2)
    otp = str(random_integer % 1000000).zfill(6)
    return otp

# ✅ Alias so old imports don't break
def generate_otp() -> str:
    return generate_quantum_otp()


def send_email(to_email: str, subject: str, body: str) -> bool:
    sender = "bhanualluri2006@gmail.com"
    password = "bdrjcpycikwpvybk"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Email error:", e)
        return False
