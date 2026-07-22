(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (helper s index)
    (if (null? s)
        '()
        (cons (list index (car s))
              (helper (cdr s) (+ index 1))
        )
    )
  )
  (helper s 0)
)
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to INORDER? and return
;; the merged lists.
(define (merge inorder? list1 list2)
  ; BEGIN PROBLEM 16
  (define (helper lst1 lst2)
    (cond ((and (null? lst1) (null? lst2)) '())
          ((null? lst1) lst2)
          ((null? lst2) lst1)
          ((inorder? (car lst1) (car lst2))
           (cons (car lst1) (helper (cdr lst1) lst2)))
          (else (cons (car lst2) (helper lst1 (cdr lst2)))
          )
    )
  )
  (helper list1 list2)
)
  ; END PROBLEM 16


;; Optional Problem 1

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           'replace-this-line
           ; END PROBLEM 17
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           'replace-this-line
           ; END PROBLEM 17
           ))
        (else
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )))



;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'replace-this-line
  )
  ; END Question 21