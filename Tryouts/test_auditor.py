class AuditorPrueba:
    def __init__(self, target):
        self.target = target    # Store the target domain into an instance attribute
        pass

    def execute_analysis(self):
        print("Stating audit analysis in: "+ str(self.target))   # 1. Print analysis start notification
        if self.target:                                # 2. Validate target attribute
            print({"target": self.target, "status": "completed"}) # 3. Return status result dictionary
        else:
            print({"target": self.target, "status": "failed"})
        pass

if __name__ == '__main__':
    auditor = AuditorPrueba("ejemplo.com")      # 1. Instantiate the class with a mock target domain
    result = auditor.execute_analysis()         # 2. Run the analysis method and print the returned dictionary
    print(result) 

# Test 2: Empty audit for else output
    auditor_vacio = AuditorPrueba("")
    print(auditor_vacio.execute_analysis())
                               
    pass