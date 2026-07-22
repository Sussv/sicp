;;; Homework 09: Macro

; ANSWER QUESTION wwsd

;;; Required Problems

(define (find n lst)
  (define (f n lst position)
    (if (= n (car lst))
        position
        (f n (cdr lst) (+ 1 position))
    )
  )
  (f n lst 0)
)


(define (find-nest n sym)
  (define (f n sym-val current)
    (cond ((and (number? (car sym-val)) (null? (cdr sym-val))) 
           (if (= n (car sym-val))
              `(car ,current)
              '()
           )
          )
          ((and (number? (car sym-val)) (not (null? (cdr sym-val))))
           (if (= n (car sym-val))
              `(car ,current)
               (f n (cdr sym-val) `(cdr ,current))
           )
          )
          ((and (not (number? (car sym-val))) (null? (cdr sym-val)))
           (f n (car sym-val) `(car ,current))
          )
          (else (append (f n (cdr sym-val) `(cdr ,current)) 
                        (f n (car sym-val) `(car ,current))
                )
          )
    )
  )
  (f n (eval sym) sym)
)


(define-macro (my/or operands)
  (cond ((null? operands) #f)
        ((null? (cdr operands)) (car operands))
        (else `(let ((t ,(car operands)))
                    (if t
                        t
                        (my/or ,(cdr operands))
                    )
                )
        )
  )
)

(define-macro (k-curry fn args vals indices)
  (define (f args vals indices i parameters body)
    (cond
          ((null? args) (cons parameters body))
          ((and (not (null? indices)) (= i (car indices)))
           (f (cdr args)
              (cdr vals)
              (cdr indices)
              (+ i 1)
              parameters
              (append body (list (car vals)))
           )
          )
          (else
                (f (cdr args)
                   vals
                   indices
                   (+ i 1)
                   (append parameters (list (car args)))
                   (append body (list (car args))))
      )
    )
  )

  (let ((result (f args vals indices 0 '() '())))
      `(lambda ,(car result) ,(cons fn (cdr result)))
  )
)

(define-macro (let* bindings expr)
  (define (f binding body)
    (if (null? binding)
        (list 'let () body)
        (list 'let (list (car binding)) (f (cdr binding) body))
    )
  )
  (f bindings expr)
)

;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)
