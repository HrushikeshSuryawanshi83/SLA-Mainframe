IDENTIFICATION DIVISION.
       PROGRAM-ID. GOODUPDT.
       
       PROCEDURE DIVISION.
       MAIN-LOGIC.
           DISPLAY 'STARTING OPTIMIZED PROCESSING...'.

           * --- EFFICIENT SQL (Only 2 calls) ---
           EXEC SQL SELECT NAME FROM EMPLOYEE WHERE ID=1 END-EXEC.
           EXEC SQL COMMIT END-EXEC.

           * --- EFFICIENT I/O (Only 1 Read) ---
           READ FILE-IN.

           * --- SIMPLE LOGIC (No complex loops) ---
           DISPLAY 'PROCESS COMPLETE'.

           STOP RUN.