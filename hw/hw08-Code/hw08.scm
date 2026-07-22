;;; Homework 08: Scheme

;;; Required Problems

(define (square x) (* x x))

;; Problem 1: Quick Pow

(define (quick-pow base exp)
  (if (= 0 exp) 
      1
      (if (even? exp)
          (square (quick-pow base (/ exp 2)))
          (* (square (quick-pow base (/ (- exp 1) 2))) base)
      )     
  )
)

;; Problem 2: Quicker Pow

(define (quicker-pow base exp)
  (define (helper di zhi result)
    (if (= zhi 0)
        result  
        (if (even? zhi)
            (helper (square di) (/ zhi 2) result)
            (helper (square di) (/ (- zhi 1) 2) (* result di))
        )
    )
            
  )
  (helper base exp 1)
)

;; Problem 3: Find

(define (find predicate lst)
  (if (equal? lst nil)
      #f
      (if (predicate (car lst))
          (car lst)
          (find predicate (cdr lst))
      )
  ) 
)

;; Problem 4: Count Change III

(define (make-change total biggest)
  (if (= total 0)
      (list '())
      (if (or (< total 0) (= biggest 0))
          '()
          (append (map (lambda (change) (cons biggest change))
                       (make-change (- total biggest) biggest)
                  )
            (make-change total (- biggest 1))
          )
      )
  )
)

;; Problem 5: Enumerate

(define (enumerate lst)
  (define (helper lst i)
    (if (null? lst)
        '()  
        (cons (cons i (car lst))
              (helper (cdr lst) (+ i 1))
        )
    )
  )
  (helper lst 0)
)

;; Problem 6: Substitute

(define (substitute bindings s)
  (define (replace x)
    (if (find (lambda (b) (eq? (car b) x)) bindings)
        (cdr (find (lambda (b) (eq? (car b) x)) bindings))
        x
    )
  )
  (if (null? s)
      '()
      (if (not (pair? s))
          (replace s)
          (cons (substitute bindings (car s))
                (substitute bindings (cdr s))
          )
      )
  )
)

;; Problem 7: Tree in Scheme

(define (tree label branches)
  (cons label branches)
)

(define (label t)
  (car t)
)

(define (branches t)
  (cdr t)
)

(define (is-leaf t)
  (if (null? (branches t))
      #t
      #f
  )
)

; A tree for test

(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 5 nil)
        (tree 6 (list
          (tree 8 nil)))))
    (tree 3 nil)
    (tree 4
      (list
        (tree 7 nil))))))

;; Problem 8: Label Sum

(define (label-sum t)
  (define (sum f x)
    (if (null? x)
        0
        (+ (f (car x)) 
           (sum f (cdr x))
        )
    )
  )
  (if (is-leaf t)
      (label t)
      (+ (label t) 
         (sum label-sum (branches t))
      )
  )
)

;;; Just For Fun Problems

;; Problem 9: Derive

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (first-operand s) (cadr s))
(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
; You can access the operands from the expressions with
; first-operand and second-operand (already defined for sum).
; (define (first-operand p) (cadr p))
; (define (second-operand p) (caddr p))

;; Problem 9.1: Derive Sum

(define (derive-sum expr var)
  'YOUR-CODE-HERE
)

;; Problem 9.2: Derive Product

(define (derive-product expr var)
  'YOUR-CODE-HERE
)

;; Problem 9.3: Make Exp

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  'YOUR-CODE-HERE
)

(define (exp? exp)
  'YOUR-CODE-HERE
)

; Some expressions for test
(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

;; Problem 9.4: Derive Exp

(define (derive-exp exp var)
  'YOUR-CODE-HERE
)
