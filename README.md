# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` to use its AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.94</td>
    <td align="right">4.47</td>
    <td align="right">3.56</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.38</td>
    <td align="right">9.84</td>
    <td align="right">15.80</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.75</td>
    <td align="right">4.06</td>
    <td align="right">4.05</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">4.79</td>
    <td align="right">5.03</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">15.63</td>
    <td align="right">14.39</td>
    <td align="right">16.68</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.47</td>
    <td align="right">4.57</td>
    <td align="right">4.60</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.44</td>
    <td align="right">7.70</td>
    <td align="right">7.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.02</td>
    <td align="right">17.58</td>
    <td align="right">15.87</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.11</td>
    <td align="right">5.05</td>
    <td align="right">5.16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">8.79</td>
    <td align="right">12.34</td>
    <td align="right">12.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">25.73</td>
    <td align="right">22.28</td>
    <td align="right">16.39</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.13</td>
    <td align="right">5.67</td>
    <td align="right">5.66</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">10.94</td>
    <td align="right">14.50</td>
    <td align="right">14.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">12.40</td>
    <td align="right">9.66</td>
    <td align="right">9.47</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.53</td>
    <td align="right">4.75</td>
    <td align="right">4.75</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.21</td>
    <td align="right">5.93</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.30</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.09</td>
    <td align="right">5.15</td>
    <td align="right">5.14</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.61</td>
    <td align="right">9.18</td>
    <td align="right">9.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">16.30</td>
    <td align="right">10.69</td>
    <td align="right">9.87</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.94</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.82</td>
    <td align="right">13.04</td>
    <td align="right">13.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">16.91</td>
    <td align="right">10.66</td>
    <td align="right">9.87</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.50</td>
    <td align="right">6.37</td>
    <td align="right">6.40</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.60</td>
    <td align="right">16.49</td>
    <td align="right">16.40</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.87</td>
    <td align="right">19.17</td>
    <td align="right">7.14</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.90</td>
    <td align="right">13.08</td>
    <td align="right">17.79</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.85</td>
    <td align="right">5.19</td>
    <td align="right">5.18</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.10</td>
    <td align="right">6.90</td>
    <td align="right">6.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.67</td>
    <td align="right">17.95</td>
    <td align="right">18.01</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.35</td>
    <td align="right">5.48</td>
    <td align="right">5.45</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.80</td>
    <td align="right">9.73</td>
    <td align="right">9.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">24.69</td>
    <td align="right">24.74</td>
    <td align="right">19.95</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">14.04</td>
    <td align="right">8.15</td>
    <td align="right">7.28</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.91</td>
    <td align="right">15.36</td>
    <td align="right">15.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">40.49</td>
    <td align="right">35.02</td>
    <td align="right">19.77</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.72</td>
    <td align="right">14.09</td>
    <td align="right">15.82</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">25.31</td>
    <td align="right">20.98</td>
    <td align="right">18.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">12.19</td>
    <td align="right">9.49</td>
    <td align="right">9.50</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.74</td>
    <td align="right">5.93</td>
    <td align="right">5.94</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.61</td>
    <td align="right">8.05</td>
    <td align="right">8.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.83</td>
    <td align="right">3.53</td>
    <td align="right">3.51</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.14</td>
    <td align="right">6.16</td>
    <td align="right">6.18</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.24</td>
    <td align="right">10.91</td>
    <td align="right">10.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">17.32</td>
    <td align="right">11.36</td>
    <td align="right">11.14</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.38</td>
    <td align="right">7.32</td>
    <td align="right">7.29</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.66</td>
    <td align="right">16.18</td>
    <td align="right">17.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">22.65</td>
    <td align="right">15.90</td>
    <td align="right">13.32</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.46</td>
    <td align="right">8.61</td>
    <td align="right">8.68</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.55</td>
    <td align="right">24.46</td>
    <td align="right">23.11</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.28</td>
    <td align="right">4.21</td>
    <td align="right">3.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.75</td>
    <td align="right">8.21</td>
    <td align="right">14.60</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.13</td>
    <td align="right">3.81</td>
    <td align="right">3.70</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.87</td>
    <td align="right">3.33</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.17</td>
    <td align="right">12.61</td>
    <td align="right">15.91</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.68</td>
    <td align="right">4.36</td>
    <td align="right">4.52</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.53</td>
    <td align="right">3.20</td>
    <td align="right">3.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.47</td>
    <td align="right">15.74</td>
    <td align="right">15.36</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.22</td>
    <td align="right">4.92</td>
    <td align="right">4.93</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.30</td>
    <td align="right">6.04</td>
    <td align="right">5.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.32</td>
    <td align="right">19.57</td>
    <td align="right">15.72</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.77</td>
    <td align="right">5.77</td>
    <td align="right">5.76</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.68</td>
    <td align="right">6.70</td>
    <td align="right">6.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">10.48</td>
    <td align="right">9.06</td>
    <td align="right">9.07</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.72</td>
    <td align="right">4.40</td>
    <td align="right">4.32</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.97</td>
    <td align="right">3.27</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.02</td>
    <td align="right">2.13</td>
    <td align="right">2.13</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.34</td>
    <td align="right">5.08</td>
    <td align="right">5.07</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.49</td>
    <td align="right">3.50</td>
    <td align="right">3.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">10.63</td>
    <td align="right">9.98</td>
    <td align="right">3.41</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.86</td>
    <td align="right">5.89</td>
    <td align="right">5.89</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.60</td>
    <td align="right">5.78</td>
    <td align="right">5.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.54</td>
    <td align="right">4.43</td>
    <td align="right">3.51</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.83</td>
    <td align="right">3.14</td>
    <td align="right">3.16</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.24</td>
    <td align="right">6.81</td>
    <td align="right">6.83</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.33</td>
    <td align="right">16.07</td>
    <td align="right">5.87</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.06</td>
    <td align="right">10.73</td>
    <td align="right">15.30</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.95</td>
    <td align="right">4.70</td>
    <td align="right">4.63</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.66</td>
    <td align="right">4.29</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.42</td>
    <td align="right">15.08</td>
    <td align="right">16.96</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.32</td>
    <td align="right">4.99</td>
    <td align="right">5.19</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.11</td>
    <td align="right">3.81</td>
    <td align="right">3.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">19.33</td>
    <td align="right">19.22</td>
    <td align="right">16.58</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.12</td>
    <td align="right">5.83</td>
    <td align="right">5.74</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.78</td>
    <td align="right">7.67</td>
    <td align="right">7.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">28.12</td>
    <td align="right">29.34</td>
    <td align="right">17.05</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">6.84</td>
    <td align="right">7.75</td>
    <td align="right">7.45</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">7.45</td>
    <td align="right">9.67</td>
    <td align="right">9.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">10.57</td>
    <td align="right">9.11</td>
    <td align="right">9.12</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.59</td>
    <td align="right">5.40</td>
    <td align="right">5.29</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.71</td>
    <td align="right">4.16</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.48</td>
    <td align="right">2.58</td>
    <td align="right">2.63</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.01</td>
    <td align="right">5.75</td>
    <td align="right">5.74</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.01</td>
    <td align="right">4.16</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.86</td>
    <td align="right">10.32</td>
    <td align="right">4.40</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.71</td>
    <td align="right">6.77</td>
    <td align="right">6.85</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">6.88</td>
    <td align="right">7.49</td>
    <td align="right">7.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">6.46</td>
    <td align="right">11.39</td>
    <td align="right">5.39</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.01</td>
    <td align="right">4.88</td>
    <td align="right">4.48</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">8.17</td>
    <td align="right">9.40</td>
    <td align="right">9.72</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.04</td>
    <td align="right">5.20</td>
    <td align="right">4.05</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.81</td>
    <td align="right">5.43</td>
    <td align="right">13.48</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.56</td>
    <td align="right">1.47</td>
    <td align="right">1.39</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.65</td>
    <td align="right">1.97</td>
    <td align="right">2.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.55</td>
    <td align="right">8.35</td>
    <td align="right">14.18</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.64</td>
    <td align="right">1.68</td>
    <td align="right">1.61</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.72</td>
    <td align="right">2.30</td>
    <td align="right">2.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.01</td>
    <td align="right">10.44</td>
    <td align="right">12.94</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.98</td>
    <td align="right">1.88</td>
    <td align="right">2.02</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.05</td>
    <td align="right">3.23</td>
    <td align="right">3.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.27</td>
    <td align="right">12.39</td>
    <td align="right">13.35</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.90</td>
    <td align="right">2.27</td>
    <td align="right">2.37</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.50</td>
    <td align="right">4.63</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.39</td>
    <td align="right">2.20</td>
    <td align="right">2.14</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">2.06</td>
    <td align="right">1.62</td>
    <td align="right">1.64</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.82</td>
    <td align="right">2.22</td>
    <td align="right">2.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.95</td>
    <td align="right">1.69</td>
    <td align="right">1.72</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.06</td>
    <td align="right">1.78</td>
    <td align="right">1.78</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.56</td>
    <td align="right">2.89</td>
    <td align="right">2.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.66</td>
    <td align="right">3.68</td>
    <td align="right">2.76</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.14</td>
    <td align="right">2.20</td>
    <td align="right">2.17</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.29</td>
    <td align="right">3.67</td>
    <td align="right">3.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.66</td>
    <td align="right">4.56</td>
    <td align="right">2.63</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.22</td>
    <td align="right">1.96</td>
    <td align="right">1.91</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.25</td>
    <td align="right">4.48</td>
    <td align="right">4.33</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">36.35</td>
    <td align="right">18.91</td>
    <td align="right">11.36</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.75</td>
    <td align="right">12.49</td>
    <td align="right">23.82</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.32</td>
    <td align="right">6.12</td>
    <td align="right">5.71</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.28</td>
    <td align="right">5.00</td>
    <td align="right">5.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">31.61</td>
    <td align="right">29.89</td>
    <td align="right">27.95</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.10</td>
    <td align="right">9.29</td>
    <td align="right">9.07</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.67</td>
    <td align="right">13.67</td>
    <td align="right">12.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">64.17</td>
    <td align="right">48.22</td>
    <td align="right">22.31</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">8.24</td>
    <td align="right">7.59</td>
    <td align="right">7.60</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.36</td>
    <td align="right">12.59</td>
    <td align="right">12.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">67.60</td>
    <td align="right">50.79</td>
    <td align="right">24.55</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.10</td>
    <td align="right">9.59</td>
    <td align="right">10.34</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">19.98</td>
    <td align="right">16.08</td>
    <td align="right">16.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.01</td>
    <td align="right">4.39</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.07</td>
    <td align="right">3.76</td>
    <td align="right">3.64</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.38</td>
    <td align="right">3.66</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.00</td>
    <td align="right">6.26</td>
    <td align="right">5.86</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.42</td>
    <td align="right">5.95</td>
    <td align="right">5.25</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.50</td>
    <td align="right">8.75</td>
    <td align="right">7.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">11.33</td>
    <td align="right">10.09</td>
    <td align="right">8.37</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.79</td>
    <td align="right">8.76</td>
    <td align="right">9.02</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">13.36</td>
    <td align="right">12.53</td>
    <td align="right">13.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">13.42</td>
    <td align="right">14.87</td>
    <td align="right">8.18</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.29</td>
    <td align="right">7.46</td>
    <td align="right">8.18</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.64</td>
    <td align="right">20.00</td>
    <td align="right">17.85</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.67</td>
    <td align="right">5.88</td>
    <td align="right">3.65</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.33</td>
    <td align="right">12.81</td>
    <td align="right">17.36</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.91</td>
    <td align="right">4.41</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">8.00</td>
    <td align="right">5.63</td>
    <td align="right">5.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.63</td>
    <td align="right">17.93</td>
    <td align="right">17.91</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.04</td>
    <td align="right">5.03</td>
    <td align="right">4.82</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.75</td>
    <td align="right">8.63</td>
    <td align="right">8.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.76</td>
    <td align="right">21.43</td>
    <td align="right">17.25</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.69</td>
    <td align="right">5.43</td>
    <td align="right">5.41</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.66</td>
    <td align="right">11.03</td>
    <td align="right">11.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.13</td>
    <td align="right">27.33</td>
    <td align="right">17.21</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">10.10</td>
    <td align="right">6.01</td>
    <td align="right">6.00</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">19.79</td>
    <td align="right">14.62</td>
    <td align="right">14.82</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">9.00</td>
    <td align="right">10.11</td>
    <td align="right">10.06</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.05</td>
    <td align="right">5.34</td>
    <td align="right">5.38</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.37</td>
    <td align="right">6.11</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.93</td>
    <td align="right">5.00</td>
    <td align="right">4.22</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.13</td>
    <td align="right">6.19</td>
    <td align="right">6.15</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.88</td>
    <td align="right">8.82</td>
    <td align="right">8.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">8.46</td>
    <td align="right">10.23</td>
    <td align="right">5.60</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.47</td>
    <td align="right">6.69</td>
    <td align="right">6.77</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.16</td>
    <td align="right">10.59</td>
    <td align="right">11.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">9.47</td>
    <td align="right">10.07</td>
    <td align="right">5.74</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.54</td>
    <td align="right">7.76</td>
    <td align="right">7.56</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.24</td>
    <td align="right">12.88</td>
    <td align="right">13.82</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">48.92</td>
    <td align="right">22.97</td>
    <td align="right">13.03</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.79</td>
    <td align="right">13.59</td>
    <td align="right">18.25</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.60</td>
    <td align="right">4.73</td>
    <td align="right">4.65</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">10.53</td>
    <td align="right">6.59</td>
    <td align="right">6.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">34.46</td>
    <td align="right">33.22</td>
    <td align="right">20.64</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">14.22</td>
    <td align="right">11.59</td>
    <td align="right">7.42</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">17.39</td>
    <td align="right">11.35</td>
    <td align="right">14.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">70.48</td>
    <td align="right">52.53</td>
    <td align="right">21.40</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.78</td>
    <td align="right">15.70</td>
    <td align="right">14.63</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">27.47</td>
    <td align="right">19.92</td>
    <td align="right">24.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">100.36</td>
    <td align="right">101.77</td>
    <td align="right">26.71</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">20.93</td>
    <td align="right">17.60</td>
    <td align="right">18.24</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">40.27</td>
    <td align="right">36.53</td>
    <td align="right">30.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">9.10</td>
    <td align="right">10.17</td>
    <td align="right">10.18</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.97</td>
    <td align="right">5.68</td>
    <td align="right">5.68</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.63</td>
    <td align="right">6.57</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.17</td>
    <td align="right">6.71</td>
    <td align="right">5.72</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.45</td>
    <td align="right">11.65</td>
    <td align="right">11.85</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">20.33</td>
    <td align="right">10.46</td>
    <td align="right">10.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.82</td>
    <td align="right">20.04</td>
    <td align="right">13.30</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">15.52</td>
    <td align="right">12.42</td>
    <td align="right">13.82</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">27.50</td>
    <td align="right">19.29</td>
    <td align="right">19.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">18.73</td>
    <td align="right">27.10</td>
    <td align="right">19.37</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">27.67</td>
    <td align="right">23.49</td>
    <td align="right">26.31</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">58.72</td>
    <td align="right">40.97</td>
    <td align="right">41.79</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.69</td>
    <td align="right">30.57</td>
    <td align="right">14.42</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.49</td>
    <td align="right">42.20</td>
    <td align="right">36.53</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.48</td>
    <td align="right">16.00</td>
    <td align="right">15.98</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.24</td>
    <td align="right">20.48</td>
    <td align="right">20.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.21</td>
    <td align="right">63.98</td>
    <td align="right">39.49</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.27</td>
    <td align="right">19.39</td>
    <td align="right">19.22</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.34</td>
    <td align="right">26.66</td>
    <td align="right">26.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.75</td>
    <td align="right">77.71</td>
    <td align="right">38.15</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.29</td>
    <td align="right">18.57</td>
    <td align="right">18.43</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.91</td>
    <td align="right">33.18</td>
    <td align="right">33.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">55.89</td>
    <td align="right">96.24</td>
    <td align="right">37.43</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.21</td>
    <td align="right">18.80</td>
    <td align="right">18.77</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">35.12</td>
    <td align="right">37.60</td>
    <td align="right">37.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.52</td>
    <td align="right">13.56</td>
    <td align="right">13.55</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.06</td>
    <td align="right">19.68</td>
    <td align="right">19.72</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.50</td>
    <td align="right">22.09</td>
    <td align="right">22.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.83</td>
    <td align="right">16.48</td>
    <td align="right">15.88</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.04</td>
    <td align="right">18.61</td>
    <td align="right">18.63</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.49</td>
    <td align="right">28.93</td>
    <td align="right">28.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.47</td>
    <td align="right">19.44</td>
    <td align="right">19.40</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.07</td>
    <td align="right">18.61</td>
    <td align="right">18.32</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.61</td>
    <td align="right">45.82</td>
    <td align="right">45.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">24.32</td>
    <td align="right">25.60</td>
    <td align="right">25.49</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.89</td>
    <td align="right">19.92</td>
    <td align="right">19.92</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.53</td>
    <td align="right">55.36</td>
    <td align="right">55.34</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">71.66</td>
    <td align="right">100.28</td>
    <td align="right">21.15</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.90</td>
    <td align="right">43.61</td>
    <td align="right">39.44</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.81</td>
    <td align="right">16.19</td>
    <td align="right">16.23</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.70</td>
    <td align="right">20.63</td>
    <td align="right">20.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">37.12</td>
    <td align="right">63.47</td>
    <td align="right">41.99</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.20</td>
    <td align="right">19.49</td>
    <td align="right">20.27</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.79</td>
    <td align="right">25.82</td>
    <td align="right">25.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">46.74</td>
    <td align="right">89.57</td>
    <td align="right">42.54</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.29</td>
    <td align="right">21.82</td>
    <td align="right">19.07</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.41</td>
    <td align="right">36.58</td>
    <td align="right">41.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">59.97</td>
    <td align="right">100.62</td>
    <td align="right">41.47</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">19.19</td>
    <td align="right">20.43</td>
    <td align="right">20.84</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">37.29</td>
    <td align="right">41.46</td>
    <td align="right">42.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.73</td>
    <td align="right">13.78</td>
    <td align="right">13.81</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.28</td>
    <td align="right">19.89</td>
    <td align="right">19.87</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.15</td>
    <td align="right">22.78</td>
    <td align="right">22.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.68</td>
    <td align="right">16.30</td>
    <td align="right">16.02</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.42</td>
    <td align="right">18.78</td>
    <td align="right">19.03</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.49</td>
    <td align="right">29.61</td>
    <td align="right">29.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.59</td>
    <td align="right">21.57</td>
    <td align="right">19.00</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">18.22</td>
    <td align="right">20.82</td>
    <td align="right">23.36</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.72</td>
    <td align="right">72.16</td>
    <td align="right">67.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">54.03</td>
    <td align="right">59.53</td>
    <td align="right">37.54</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">32.55</td>
    <td align="right">47.09</td>
    <td align="right">48.08</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">105.68</td>
    <td align="right">102.11</td>
    <td align="right">95.98</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.80</td>
    <td align="right">10.13</td>
    <td align="right">7.00</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.78</td>
    <td align="right">23.06</td>
    <td align="right">26.68</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.44</td>
    <td align="right">12.29</td>
    <td align="right">12.30</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.98</td>
    <td align="right">16.14</td>
    <td align="right">16.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.46</td>
    <td align="right">35.01</td>
    <td align="right">29.16</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.35</td>
    <td align="right">14.37</td>
    <td align="right">14.06</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.38</td>
    <td align="right">22.43</td>
    <td align="right">22.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.86</td>
    <td align="right">47.56</td>
    <td align="right">30.16</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.74</td>
    <td align="right">15.53</td>
    <td align="right">15.40</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.13</td>
    <td align="right">32.13</td>
    <td align="right">32.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.48</td>
    <td align="right">60.58</td>
    <td align="right">30.27</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.61</td>
    <td align="right">16.37</td>
    <td align="right">16.31</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">30.26</td>
    <td align="right">37.14</td>
    <td align="right">37.11</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.04</td>
    <td align="right">9.39</td>
    <td align="right">9.41</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.80</td>
    <td align="right">13.89</td>
    <td align="right">13.83</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.19</td>
    <td align="right">16.59</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">10.89</td>
    <td align="right">13.90</td>
    <td align="right">13.99</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.50</td>
    <td align="right">15.33</td>
    <td align="right">15.36</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.79</td>
    <td align="right">22.41</td>
    <td align="right">22.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.39</td>
    <td align="right">17.56</td>
    <td align="right">17.54</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.64</td>
    <td align="right">16.76</td>
    <td align="right">16.82</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.67</td>
    <td align="right">30.92</td>
    <td align="right">31.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">17.27</td>
    <td align="right">22.05</td>
    <td align="right">22.11</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">16.15</td>
    <td align="right">17.90</td>
    <td align="right">17.85</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.96</td>
    <td align="right">35.76</td>
    <td align="right">35.76</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">80.05</td>
    <td align="right">49.69</td>
    <td align="right">10.89</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.29</td>
    <td align="right">23.17</td>
    <td align="right">28.78</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.82</td>
    <td align="right">12.85</td>
    <td align="right">12.81</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.36</td>
    <td align="right">17.10</td>
    <td align="right">17.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.52</td>
    <td align="right">34.84</td>
    <td align="right">30.04</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.04</td>
    <td align="right">13.95</td>
    <td align="right">13.98</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.07</td>
    <td align="right">22.24</td>
    <td align="right">22.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.97</td>
    <td align="right">48.28</td>
    <td align="right">30.79</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.80</td>
    <td align="right">16.70</td>
    <td align="right">19.18</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.80</td>
    <td align="right">40.57</td>
    <td align="right">39.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">57.26</td>
    <td align="right">67.74</td>
    <td align="right">32.47</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">17.82</td>
    <td align="right">18.89</td>
    <td align="right">18.65</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">33.24</td>
    <td align="right">42.85</td>
    <td align="right">41.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.38</td>
    <td align="right">9.77</td>
    <td align="right">9.74</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.11</td>
    <td align="right">14.22</td>
    <td align="right">14.19</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.61</td>
    <td align="right">18.07</td>
    <td align="right">18.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.51</td>
    <td align="right">14.16</td>
    <td align="right">16.11</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">15.53</td>
    <td align="right">17.11</td>
    <td align="right">17.08</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.31</td>
    <td align="right">22.28</td>
    <td align="right">22.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.69</td>
    <td align="right">17.98</td>
    <td align="right">19.49</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.94</td>
    <td align="right">18.74</td>
    <td align="right">19.61</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.40</td>
    <td align="right">32.05</td>
    <td align="right">31.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">20.50</td>
    <td align="right">26.28</td>
    <td align="right">26.43</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">18.15</td>
    <td align="right">20.04</td>
    <td align="right">20.38</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">36.18</td>
    <td align="right">41.43</td>
    <td align="right">39.87</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.94</td>
    <td align="right">8.72</td>
    <td align="right">8.08</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">55.95</td>
    <td align="right">53.73</td>
    <td align="right">37.08</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.09</td>
    <td align="right">17.42</td>
    <td align="right">20.63</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">20.11</td>
    <td align="right">41.60</td>
    <td align="right">41.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">85.71</td>
    <td align="right">78.34</td>
    <td align="right">38.39</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.36</td>
    <td align="right">18.71</td>
    <td align="right">20.65</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">24.62</td>
    <td align="right">56.74</td>
    <td align="right">57.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">105.74</td>
    <td align="right">96.57</td>
    <td align="right">37.24</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.53</td>
    <td align="right">19.35</td>
    <td align="right">20.53</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.72</td>
    <td align="right">77.41</td>
    <td align="right">77.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">134.04</td>
    <td align="right">120.95</td>
    <td align="right">38.25</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.65</td>
    <td align="right">20.51</td>
    <td align="right">21.28</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">41.95</td>
    <td align="right">91.47</td>
    <td align="right">91.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">19.14</td>
    <td align="right">29.27</td>
    <td align="right">29.27</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.83</td>
    <td align="right">22.36</td>
    <td align="right">24.99</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">22.92</td>
    <td align="right">40.20</td>
    <td align="right">41.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">16.03</td>
    <td align="right">32.79</td>
    <td align="right">23.69</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">24.00</td>
    <td align="right">24.10</td>
    <td align="right">25.93</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">29.33</td>
    <td align="right">56.43</td>
    <td align="right">58.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.74</td>
    <td align="right">52.89</td>
    <td align="right">37.37</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">25.99</td>
    <td align="right">26.86</td>
    <td align="right">27.54</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">42.13</td>
    <td align="right">78.20</td>
    <td align="right">78.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">26.03</td>
    <td align="right">51.33</td>
    <td align="right">38.08</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">27.31</td>
    <td align="right">28.92</td>
    <td align="right">28.76</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">48.46</td>
    <td align="right">91.95</td>
    <td align="right">93.36</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">60.65</td>
    <td align="right">37.20</td>
    <td align="right">12.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">62.37</td>
    <td align="right">57.22</td>
    <td align="right">41.24</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">19.93</td>
    <td align="right">18.31</td>
    <td align="right">22.59</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.62</td>
    <td align="right">43.64</td>
    <td align="right">41.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">92.86</td>
    <td align="right">89.51</td>
    <td align="right">41.76</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">23.72</td>
    <td align="right">19.79</td>
    <td align="right">22.85</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">27.58</td>
    <td align="right">59.52</td>
    <td align="right">60.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">121.83</td>
    <td align="right">130.55</td>
    <td align="right">46.66</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">30.60</td>
    <td align="right">23.09</td>
    <td align="right">27.92</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">45.41</td>
    <td align="right">83.26</td>
    <td align="right">82.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">259.59</td>
    <td align="right">230.51</td>
    <td align="right">55.66</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">56.79</td>
    <td align="right">35.84</td>
    <td align="right">43.57</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">56.93</td>
    <td align="right">113.32</td>
    <td align="right">111.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">21.01</td>
    <td align="right">35.16</td>
    <td align="right">34.87</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">24.55</td>
    <td align="right">25.36</td>
    <td align="right">29.85</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.98</td>
    <td align="right">44.49</td>
    <td align="right">44.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">18.60</td>
    <td align="right">39.89</td>
    <td align="right">28.19</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">28.15</td>
    <td align="right">28.08</td>
    <td align="right">32.01</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.82</td>
    <td align="right">71.82</td>
    <td align="right">72.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">35.20</td>
    <td align="right">81.81</td>
    <td align="right">58.45</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">44.55</td>
    <td align="right">42.86</td>
    <td align="right">50.64</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">50.04</td>
    <td align="right">84.41</td>
    <td align="right">86.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">45.16</td>
    <td align="right">94.98</td>
    <td align="right">82.64</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">59.75</td>
    <td align="right">65.50</td>
    <td align="right">65.11</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">65.67</td>
    <td align="right">112.36</td>
    <td align="right">121.83</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
