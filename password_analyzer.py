import re
import string

class passwordAnalyzer:
    def __init__(self):
        self.score = 0
        self.feedback=[]
        self.min_length = 8

    def analyze_password(self,password):
        #Main Function to analyze password strength.
        self.score = 0
        self.feedback = []

        #Check for specifics
        self._check_length(password)
        self._check_character_types(password)

        #Calculate final strength
        strength = self._calculate_strength()
        return{
            "score": self.score,
            "strength": strength,
            "feedback": self.feedback
        }

    def _check_length(self, password):
        #Check for password length
        length = len(password)
        if length < self.min_length:
            self.feedback.append(f"Password should be at least {self.min_length} characters long" )
        elif length >= 12:
            self.score += 30
        elif length >= 10:
            self.score += 20
        else:
            self.score +=10


    def _check_character_types(self, password):
        #check for different character types
        if re.search(r"[A-Z]", password):
            self.score += 15
        else:
            self.feedback.append("Add uppercase letters for better strength")

        if re.search(r"[a-z]", password):
            self.score += 15
        else:
            self.feedback.append("Add lowercase letter for better strength")

        if re.search(r"[0-9]", password):
            self.score +=15
        else:
            self.feedback.append("Add numbers for better strength")
        if re.search(r"[!@#$%^&*()_+=]", password):
            self.score += 20
        else:
            self.feedback.append("Add special characters for better strength")

    def _calculate_strength(self):
        #Calculate overall strength rating
        if self.score >= 90:
            return "Very Strong"
        if self.score >= 80:
            return "Strong" 
        elif self.score >= 60:
            return "Moderate" 
        elif self.score >= 40:
            return "Weak"
        else:
            return "Very Weak"



def test_password(password):
        #A funtion to test the password
        analyzer = passwordAnalyzer()
        result = analyzer.analyze_password(password)


        print(f"\npassword:  {password}")
        print(f"Score: {result['score']}/100") 
        print(f"Strength: {result['strength']}")
        if result['feedback']:
            print("Feedback:") 
            for item in result['feedback']:
                print(f"- {item}") 


#Axample usage
if __name__ == "__main__":
    test_passwords = [
        "pass123",
        "Password123!",
        "Ab1!",
        "SuperSecurePass123#",
        "aaa111",
        "#Apollo2020"
    ]

    for pwd in test_passwords:
        test_password(pwd)
