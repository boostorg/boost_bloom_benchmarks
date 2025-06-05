# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

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
    <td align="right">25.89</td>
    <td align="right">4.47</td>
    <td align="right">3.57</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">11.50</td>
    <td align="right">10.57</td>
    <td align="right">16.58</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.03</td>
    <td align="right">4.36</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.81</td>
    <td align="right">5.04</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.35</td>
    <td align="right">15.67</td>
    <td align="right">17.72</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.79</td>
    <td align="right">4.92</td>
    <td align="right">4.95</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.43</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.73</td>
    <td align="right">16.89</td>
    <td align="right">15.69</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.41</td>
    <td align="right">5.33</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.23</td>
    <td align="right">6.27</td>
    <td align="right">6.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.23</td>
    <td align="right">23.11</td>
    <td align="right">16.77</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.17</td>
    <td align="right">5.91</td>
    <td align="right">5.91</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.71</td>
    <td align="right">6.60</td>
    <td align="right">6.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4274</td>
    <td align="right">5.09</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.24</td>
    <td align="right">6.57</td>
    <td align="right">6.50</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.94</td>
    <td align="right">3.27</td>
    <td align="right">3.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.50</td>
    <td align="right">8.87</td>
    <td align="right">8.85</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.14</td>
    <td align="right">9.86</td>
    <td align="right">9.87</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.46</td>
    <td align="right">3.10</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.17</td>
    <td align="right">13.15</td>
    <td align="right">13.17</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.65</td>
    <td align="right">15.05</td>
    <td align="right">15.03</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.69</td>
    <td align="right">5.76</td>
    <td align="right">3.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.08</td>
    <td align="right">14.85</td>
    <td align="right">14.86</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.13</td>
    <td align="right">16.15</td>
    <td align="right">16.23</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.73</td>
    <td align="right">5.78</td>
    <td align="right">3.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4803</td>
    <td align="right">2.92</td>
    <td align="right">3.24</td>
    <td align="right">3.21</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.35</td>
    <td align="right">5.09</td>
    <td align="right">5.02</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.53</td>
    <td align="right">4.96</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.01</td>
    <td align="right">3.29</td>
    <td align="right">3.30</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.17</td>
    <td align="right">4.47</td>
    <td align="right">4.46</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.43</td>
    <td align="right">5.11</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.41</td>
    <td align="right">5.49</td>
    <td align="right">3.74</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.03</td>
    <td align="right">7.70</td>
    <td align="right">5.87</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.82</td>
    <td align="right">7.55</td>
    <td align="right">5.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.45</td>
    <td align="right">5.52</td>
    <td align="right">3.78</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.01</td>
    <td align="right">9.13</td>
    <td align="right">5.92</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.26</td>
    <td align="right">8.99</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">6.80</td>
    <td align="right">6.25</td>
    <td align="right">12.72</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.89</td>
    <td align="right">7.01</td>
    <td align="right">13.55</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.44</td>
    <td align="right">8.95</td>
    <td align="right">17.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.27</td>
    <td align="right">8.26</td>
    <td align="right">12.75</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.32</td>
    <td align="right">8.16</td>
    <td align="right">12.41</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.17</td>
    <td align="right">9.50</td>
    <td align="right">14.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.79</td>
    <td align="right">10.33</td>
    <td align="right">12.43</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.01</td>
    <td align="right">10.37</td>
    <td align="right">12.04</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.36</td>
    <td align="right">12.62</td>
    <td align="right">15.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.37</td>
    <td align="right">12.78</td>
    <td align="right">13.20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.42</td>
    <td align="right">12.73</td>
    <td align="right">13.18</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.81</td>
    <td align="right">14.15</td>
    <td align="right">14.91</td>
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
    <td align="right">29.52</td>
    <td align="right">17.09</td>
    <td align="right">6.14</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">13.26</td>
    <td align="right">12.55</td>
    <td align="right">17.43</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.71</td>
    <td align="right">5.00</td>
    <td align="right">5.01</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.69</td>
    <td align="right">5.88</td>
    <td align="right">5.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.97</td>
    <td align="right">18.20</td>
    <td align="right">18.04</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.28</td>
    <td align="right">5.40</td>
    <td align="right">5.40</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.02</td>
    <td align="right">6.06</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">24.89</td>
    <td align="right">23.23</td>
    <td align="right">17.25</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.30</td>
    <td align="right">6.15</td>
    <td align="right">6.16</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.19</td>
    <td align="right">7.27</td>
    <td align="right">7.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">35.55</td>
    <td align="right">33.19</td>
    <td align="right">17.89</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.61</td>
    <td align="right">7.56</td>
    <td align="right">7.37</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.35</td>
    <td align="right">8.16</td>
    <td align="right">8.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4515</td>
    <td align="right">5.96</td>
    <td align="right">6.73</td>
    <td align="right">6.71</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.13</td>
    <td align="right">7.68</td>
    <td align="right">7.62</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.54</td>
    <td align="right">4.03</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.26</td>
    <td align="right">9.50</td>
    <td align="right">9.43</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.74</td>
    <td align="right">10.56</td>
    <td align="right">10.56</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.85</td>
    <td align="right">3.53</td>
    <td align="right">3.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.70</td>
    <td align="right">14.24</td>
    <td align="right">14.30</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.40</td>
    <td align="right">16.54</td>
    <td align="right">16.41</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.65</td>
    <td align="right">6.83</td>
    <td align="right">4.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">13.34</td>
    <td align="right">16.26</td>
    <td align="right">16.06</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.36</td>
    <td align="right">18.36</td>
    <td align="right">18.33</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.38</td>
    <td align="right">7.71</td>
    <td align="right">5.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4625</td>
    <td align="right">3.15</td>
    <td align="right">3.39</td>
    <td align="right">3.38</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.11</td>
    <td align="right">5.98</td>
    <td align="right">5.89</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.22</td>
    <td align="right">5.86</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.43</td>
    <td align="right">3.84</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.58</td>
    <td align="right">4.98</td>
    <td align="right">4.92</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.85</td>
    <td align="right">5.69</td>
    <td align="right">5.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.16</td>
    <td align="right">6.58</td>
    <td align="right">4.69</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.10</td>
    <td align="right">9.10</td>
    <td align="right">7.10</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.00</td>
    <td align="right">9.05</td>
    <td align="right">7.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">6.93</td>
    <td align="right">7.39</td>
    <td align="right">8.21</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">9.90</td>
    <td align="right">11.48</td>
    <td align="right">7.85</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">10.21</td>
    <td align="right">11.37</td>
    <td align="right">7.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">7.98</td>
    <td align="right">7.16</td>
    <td align="right">13.11</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.01</td>
    <td align="right">8.08</td>
    <td align="right">13.98</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.53</td>
    <td align="right">10.11</td>
    <td align="right">18.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.02</td>
    <td align="right">8.91</td>
    <td align="right">12.88</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.06</td>
    <td align="right">8.72</td>
    <td align="right">12.56</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.86</td>
    <td align="right">10.11</td>
    <td align="right">14.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">12.03</td>
    <td align="right">11.47</td>
    <td align="right">12.91</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">12.21</td>
    <td align="right">11.51</td>
    <td align="right">12.48</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">16.77</td>
    <td align="right">13.93</td>
    <td align="right">15.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">16.53</td>
    <td align="right">14.30</td>
    <td align="right">14.05</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">16.59</td>
    <td align="right">14.28</td>
    <td align="right">14.01</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">21.39</td>
    <td align="right">16.64</td>
    <td align="right">15.85</td>
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
    <td align="right">27.13</td>
    <td align="right">4.26</td>
    <td align="right">3.40</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">11.67</td>
    <td align="right">8.97</td>
    <td align="right">15.38</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.67</td>
    <td align="right">3.97</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.84</td>
    <td align="right">4.63</td>
    <td align="right">4.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.22</td>
    <td align="right">13.64</td>
    <td align="right">16.56</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.11</td>
    <td align="right">4.56</td>
    <td align="right">4.56</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.45</td>
    <td align="right">5.32</td>
    <td align="right">5.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.34</td>
    <td align="right">16.70</td>
    <td align="right">15.63</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.50</td>
    <td align="right">5.08</td>
    <td align="right">5.27</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.64</td>
    <td align="right">6.00</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.24</td>
    <td align="right">22.75</td>
    <td align="right">15.91</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.58</td>
    <td align="right">5.68</td>
    <td align="right">5.87</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.86</td>
    <td align="right">3.34</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4274</td>
    <td align="right">3.07</td>
    <td align="right">3.61</td>
    <td align="right">3.64</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.19</td>
    <td align="right">3.55</td>
    <td align="right">3.54</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.61</td>
    <td align="right">2.55</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.75</td>
    <td align="right">4.11</td>
    <td align="right">4.08</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.77</td>
    <td align="right">4.37</td>
    <td align="right">4.44</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.18</td>
    <td align="right">2.28</td>
    <td align="right">2.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.60</td>
    <td align="right">8.29</td>
    <td align="right">7.18</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.80</td>
    <td align="right">7.02</td>
    <td align="right">7.02</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.22</td>
    <td align="right">4.41</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.05</td>
    <td align="right">7.63</td>
    <td align="right">7.62</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.31</td>
    <td align="right">8.15</td>
    <td align="right">8.12</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.21</td>
    <td align="right">4.43</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4803</td>
    <td align="right">2.62</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.65</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.72</td>
    <td align="right">3.96</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.73</td>
    <td align="right">2.44</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.96</td>
    <td align="right">3.76</td>
    <td align="right">3.77</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.87</td>
    <td align="right">4.08</td>
    <td align="right">4.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.23</td>
    <td align="right">4.29</td>
    <td align="right">2.98</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.71</td>
    <td align="right">6.08</td>
    <td align="right">4.70</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.82</td>
    <td align="right">6.01</td>
    <td align="right">4.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.31</td>
    <td align="right">4.36</td>
    <td align="right">2.96</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.63</td>
    <td align="right">7.13</td>
    <td align="right">4.63</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.81</td>
    <td align="right">7.07</td>
    <td align="right">4.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">6.67</td>
    <td align="right">6.10</td>
    <td align="right">12.42</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.82</td>
    <td align="right">6.07</td>
    <td align="right">12.19</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.49</td>
    <td align="right">7.97</td>
    <td align="right">16.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.30</td>
    <td align="right">8.51</td>
    <td align="right">12.34</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.44</td>
    <td align="right">8.21</td>
    <td align="right">12.19</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.73</td>
    <td align="right">9.61</td>
    <td align="right">13.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.89</td>
    <td align="right">9.93</td>
    <td align="right">12.08</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.60</td>
    <td align="right">9.93</td>
    <td align="right">11.81</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.90</td>
    <td align="right">12.38</td>
    <td align="right">14.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.43</td>
    <td align="right">12.29</td>
    <td align="right">12.80</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.86</td>
    <td align="right">12.28</td>
    <td align="right">12.81</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.82</td>
    <td align="right">13.85</td>
    <td align="right">14.54</td>
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
    <td align="right">33.43</td>
    <td align="right">16.89</td>
    <td align="right">7.64</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">10.96</td>
    <td align="right">10.55</td>
    <td align="right">16.31</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.58</td>
    <td align="right">4.53</td>
    <td align="right">4.71</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.86</td>
    <td align="right">5.31</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.81</td>
    <td align="right">16.11</td>
    <td align="right">17.22</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.04</td>
    <td align="right">5.33</td>
    <td align="right">5.65</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.67</td>
    <td align="right">6.13</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">31.47</td>
    <td align="right">28.72</td>
    <td align="right">16.46</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.88</td>
    <td align="right">9.20</td>
    <td align="right">9.50</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">12.79</td>
    <td align="right">10.15</td>
    <td align="right">9.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">59.46</td>
    <td align="right">62.74</td>
    <td align="right">21.83</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.89</td>
    <td align="right">16.58</td>
    <td align="right">15.28</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.59</td>
    <td align="right">8.47</td>
    <td align="right">9.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4515</td>
    <td align="right">3.64</td>
    <td align="right">4.24</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.72</td>
    <td align="right">4.16</td>
    <td align="right">4.12</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.99</td>
    <td align="right">2.96</td>
    <td align="right">2.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.46</td>
    <td align="right">5.43</td>
    <td align="right">5.72</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.53</td>
    <td align="right">5.62</td>
    <td align="right">5.63</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.95</td>
    <td align="right">3.31</td>
    <td align="right">2.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">8.07</td>
    <td align="right">12.07</td>
    <td align="right">11.63</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">8.59</td>
    <td align="right">10.49</td>
    <td align="right">10.54</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.64</td>
    <td align="right">11.43</td>
    <td align="right">7.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.40</td>
    <td align="right">21.14</td>
    <td align="right">19.53</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">13.62</td>
    <td align="right">21.29</td>
    <td align="right">22.14</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">12.52</td>
    <td align="right">13.31</td>
    <td align="right">9.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4625</td>
    <td align="right">3.08</td>
    <td align="right">2.93</td>
    <td align="right">2.88</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.28</td>
    <td align="right">4.83</td>
    <td align="right">4.83</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.33</td>
    <td align="right">4.66</td>
    <td align="right">4.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.35</td>
    <td align="right">3.12</td>
    <td align="right">2.98</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.65</td>
    <td align="right">4.67</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.60</td>
    <td align="right">4.98</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.90</td>
    <td align="right">8.63</td>
    <td align="right">5.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">9.08</td>
    <td align="right">9.46</td>
    <td align="right">7.18</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.52</td>
    <td align="right">8.34</td>
    <td align="right">6.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.07</td>
    <td align="right">13.25</td>
    <td align="right">7.81</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">15.22</td>
    <td align="right">18.79</td>
    <td align="right">14.40</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">18.52</td>
    <td align="right">21.28</td>
    <td align="right">13.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">8.34</td>
    <td align="right">8.92</td>
    <td align="right">15.78</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.87</td>
    <td align="right">7.47</td>
    <td align="right">13.66</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">14.94</td>
    <td align="right">10.54</td>
    <td align="right">18.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">17.63</td>
    <td align="right">14.27</td>
    <td align="right">17.15</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">17.42</td>
    <td align="right">13.05</td>
    <td align="right">15.99</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">23.90</td>
    <td align="right">15.69</td>
    <td align="right">17.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">29.62</td>
    <td align="right">28.86</td>
    <td align="right">18.57</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">31.15</td>
    <td align="right">29.62</td>
    <td align="right">18.91</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">42.22</td>
    <td align="right">38.22</td>
    <td align="right">23.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">25.20</td>
    <td align="right">38.52</td>
    <td align="right">21.97</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">49.18</td>
    <td align="right">39.00</td>
    <td align="right">21.76</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">62.42</td>
    <td align="right">45.14</td>
    <td align="right">23.74</td>
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
    <td align="right">21.77</td>
    <td align="right">4.17</td>
    <td align="right">3.59</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">7.23</td>
    <td align="right">5.07</td>
    <td align="right">12.46</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.43</td>
    <td align="right">1.30</td>
    <td align="right">1.25</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.64</td>
    <td align="right">1.35</td>
    <td align="right">1.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.48</td>
    <td align="right">7.60</td>
    <td align="right">12.96</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.56</td>
    <td align="right">1.51</td>
    <td align="right">1.48</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.82</td>
    <td align="right">1.55</td>
    <td align="right">1.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.66</td>
    <td align="right">9.20</td>
    <td align="right">12.19</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.78</td>
    <td align="right">1.79</td>
    <td align="right">1.78</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.87</td>
    <td align="right">1.68</td>
    <td align="right">1.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.56</td>
    <td align="right">12.29</td>
    <td align="right">12.10</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.75</td>
    <td align="right">2.69</td>
    <td align="right">2.34</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.94</td>
    <td align="right">1.77</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4274</td>
    <td align="right">2.60</td>
    <td align="right">2.01</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">4.37</td>
    <td align="right">1.91</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.07</td>
    <td align="right">1.92</td>
    <td align="right">1.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.36</td>
    <td align="right">2.17</td>
    <td align="right">2.31</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.28</td>
    <td align="right">2.54</td>
    <td align="right">2.48</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.65</td>
    <td align="right">1.50</td>
    <td align="right">1.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.43</td>
    <td align="right">3.21</td>
    <td align="right">3.19</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">9.09</td>
    <td align="right">3.14</td>
    <td align="right">3.27</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.29</td>
    <td align="right">2.70</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.76</td>
    <td align="right">4.64</td>
    <td align="right">3.92</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.40</td>
    <td align="right">4.39</td>
    <td align="right">4.31</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.28</td>
    <td align="right">3.39</td>
    <td align="right">1.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4803</td>
    <td align="right">2.13</td>
    <td align="right">1.85</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.47</td>
    <td align="right">1.90</td>
    <td align="right">1.85</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">4.70</td>
    <td align="right">1.92</td>
    <td align="right">1.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.21</td>
    <td align="right">1.81</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.42</td>
    <td align="right">1.99</td>
    <td align="right">2.34</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.29</td>
    <td align="right">2.38</td>
    <td align="right">2.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.96</td>
    <td align="right">2.45</td>
    <td align="right">2.20</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.20</td>
    <td align="right">2.99</td>
    <td align="right">2.95</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">9.81</td>
    <td align="right">3.32</td>
    <td align="right">3.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.00</td>
    <td align="right">2.90</td>
    <td align="right">1.75</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.28</td>
    <td align="right">5.06</td>
    <td align="right">3.72</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">10.11</td>
    <td align="right">3.86</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">3.55</td>
    <td align="right">3.61</td>
    <td align="right">12.63</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.32</td>
    <td align="right">3.23</td>
    <td align="right">10.29</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.00</td>
    <td align="right">5.26</td>
    <td align="right">13.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.60</td>
    <td align="right">5.46</td>
    <td align="right">11.10</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">4.66</td>
    <td align="right">4.88</td>
    <td align="right">11.27</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">8.37</td>
    <td align="right">5.10</td>
    <td align="right">11.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">6.59</td>
    <td align="right">6.13</td>
    <td align="right">11.00</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">7.93</td>
    <td align="right">6.10</td>
    <td align="right">10.99</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">10.96</td>
    <td align="right">6.86</td>
    <td align="right">12.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">8.91</td>
    <td align="right">8.78</td>
    <td align="right">12.80</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">9.17</td>
    <td align="right">7.89</td>
    <td align="right">11.89</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">12.72</td>
    <td align="right">7.73</td>
    <td align="right">12.05</td>
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
    <td align="right">28.67</td>
    <td align="right">12.56</td>
    <td align="right">8.02</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">9.51</td>
    <td align="right">8.92</td>
    <td align="right">17.88</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.41</td>
    <td align="right">3.58</td>
    <td align="right">3.70</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.97</td>
    <td align="right">2.91</td>
    <td align="right">2.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">25.82</td>
    <td align="right">25.24</td>
    <td align="right">21.28</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.27</td>
    <td align="right">4.29</td>
    <td align="right">3.78</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">2.99</td>
    <td align="right">5.49</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">45.99</td>
    <td align="right">38.39</td>
    <td align="right">23.98</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.89</td>
    <td align="right">8.33</td>
    <td align="right">9.79</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.47</td>
    <td align="right">7.91</td>
    <td align="right">8.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">68.66</td>
    <td align="right">55.06</td>
    <td align="right">27.15</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.92</td>
    <td align="right">8.70</td>
    <td align="right">9.50</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.82</td>
    <td align="right">9.63</td>
    <td align="right">8.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4515</td>
    <td align="right">3.45</td>
    <td align="right">4.56</td>
    <td align="right">3.72</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.86</td>
    <td align="right">4.45</td>
    <td align="right">3.05</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.07</td>
    <td align="right">3.95</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.39</td>
    <td align="right">4.00</td>
    <td align="right">9.68</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">23.53</td>
    <td align="right">8.01</td>
    <td align="right">8.62</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.26</td>
    <td align="right">6.91</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">14.24</td>
    <td align="right">14.27</td>
    <td align="right">10.45</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">40.75</td>
    <td align="right">10.38</td>
    <td align="right">12.36</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.66</td>
    <td align="right">10.50</td>
    <td align="right">7.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">20.88</td>
    <td align="right">17.14</td>
    <td align="right">17.18</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">52.84</td>
    <td align="right">16.05</td>
    <td align="right">17.63</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.64</td>
    <td align="right">10.20</td>
    <td align="right">7.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4625</td>
    <td align="right">2.39</td>
    <td align="right">2.59</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.71</td>
    <td align="right">2.61</td>
    <td align="right">2.62</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.38</td>
    <td align="right">2.66</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.85</td>
    <td align="right">2.93</td>
    <td align="right">2.99</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.68</td>
    <td align="right">3.97</td>
    <td align="right">5.77</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.78</td>
    <td align="right">4.60</td>
    <td align="right">5.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.50</td>
    <td align="right">7.48</td>
    <td align="right">5.28</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">9.77</td>
    <td align="right">10.30</td>
    <td align="right">8.92</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">23.19</td>
    <td align="right">9.13</td>
    <td align="right">8.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.50</td>
    <td align="right">10.26</td>
    <td align="right">6.10</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.49</td>
    <td align="right">12.83</td>
    <td align="right">12.52</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">31.40</td>
    <td align="right">13.34</td>
    <td align="right">13.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">5.11</td>
    <td align="right">4.54</td>
    <td align="right">11.19</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">4.97</td>
    <td align="right">4.21</td>
    <td align="right">11.14</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">9.05</td>
    <td align="right">5.01</td>
    <td align="right">13.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">8.38</td>
    <td align="right">7.57</td>
    <td align="right">12.27</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">8.20</td>
    <td align="right">7.23</td>
    <td align="right">11.97</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.37</td>
    <td align="right">7.65</td>
    <td align="right">12.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.56</td>
    <td align="right">13.42</td>
    <td align="right">13.34</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">14.07</td>
    <td align="right">12.13</td>
    <td align="right">13.15</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">22.11</td>
    <td align="right">14.84</td>
    <td align="right">17.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">21.56</td>
    <td align="right">17.14</td>
    <td align="right">15.17</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">19.92</td>
    <td align="right">16.36</td>
    <td align="right">15.24</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">27.65</td>
    <td align="right">19.46</td>
    <td align="right">16.54</td>
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
    <td align="right">34.26</td>
    <td align="right">5.72</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">12.13</td>
    <td align="right">12.65</td>
    <td align="right">17.07</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">6.14</td>
    <td align="right">5.49</td>
    <td align="right">5.38</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.67</td>
    <td align="right">6.39</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.30</td>
    <td align="right">17.55</td>
    <td align="right">17.78</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.37</td>
    <td align="right">5.74</td>
    <td align="right">5.81</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.53</td>
    <td align="right">7.09</td>
    <td align="right">7.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.67</td>
    <td align="right">21.61</td>
    <td align="right">17.33</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.78</td>
    <td align="right">6.39</td>
    <td align="right">6.44</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">10.19</td>
    <td align="right">9.02</td>
    <td align="right">7.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.16</td>
    <td align="right">27.77</td>
    <td align="right">17.37</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">10.07</td>
    <td align="right">7.04</td>
    <td align="right">7.25</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">11.58</td>
    <td align="right">9.02</td>
    <td align="right">9.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4274</td>
    <td align="right">8.72</td>
    <td align="right">8.25</td>
    <td align="right">8.29</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">11.89</td>
    <td align="right">8.85</td>
    <td align="right">8.77</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.38</td>
    <td align="right">3.90</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.47</td>
    <td align="right">12.43</td>
    <td align="right">11.27</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.35</td>
    <td align="right">13.00</td>
    <td align="right">12.82</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.94</td>
    <td align="right">4.89</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">16.77</td>
    <td align="right">15.38</td>
    <td align="right">15.29</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">19.34</td>
    <td align="right">17.20</td>
    <td align="right">17.22</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.96</td>
    <td align="right">6.97</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">19.31</td>
    <td align="right">17.48</td>
    <td align="right">17.54</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">22.60</td>
    <td align="right">20.18</td>
    <td align="right">20.84</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.00</td>
    <td align="right">7.15</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4803</td>
    <td align="right">3.24</td>
    <td align="right">3.83</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.52</td>
    <td align="right">5.46</td>
    <td align="right">5.50</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.66</td>
    <td align="right">5.37</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.27</td>
    <td align="right">5.54</td>
    <td align="right">4.67</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.77</td>
    <td align="right">5.88</td>
    <td align="right">5.07</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">7.02</td>
    <td align="right">7.07</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.05</td>
    <td align="right">6.84</td>
    <td align="right">5.09</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.82</td>
    <td align="right">9.46</td>
    <td align="right">7.47</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.60</td>
    <td align="right">9.44</td>
    <td align="right">7.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.16</td>
    <td align="right">7.04</td>
    <td align="right">5.14</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.38</td>
    <td align="right">10.52</td>
    <td align="right">7.60</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.06</td>
    <td align="right">10.43</td>
    <td align="right">7.66</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">9.27</td>
    <td align="right">8.75</td>
    <td align="right">13.76</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">9.32</td>
    <td align="right">8.71</td>
    <td align="right">13.60</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.58</td>
    <td align="right">11.66</td>
    <td align="right">17.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">12.20</td>
    <td align="right">11.37</td>
    <td align="right">13.01</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">12.62</td>
    <td align="right">11.15</td>
    <td align="right">13.02</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">14.38</td>
    <td align="right">12.95</td>
    <td align="right">14.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.67</td>
    <td align="right">13.88</td>
    <td align="right">13.05</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">15.21</td>
    <td align="right">14.13</td>
    <td align="right">12.72</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">18.65</td>
    <td align="right">17.60</td>
    <td align="right">15.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.26</td>
    <td align="right">17.60</td>
    <td align="right">14.01</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.51</td>
    <td align="right">17.45</td>
    <td align="right">13.46</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">21.63</td>
    <td align="right">20.48</td>
    <td align="right">15.00</td>
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
    <td align="right">41.01</td>
    <td align="right">20.34</td>
    <td align="right">7.56</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">14.75</td>
    <td align="right">13.05</td>
    <td align="right">17.73</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.19</td>
    <td align="right">5.55</td>
    <td align="right">5.62</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">9.10</td>
    <td align="right">7.17</td>
    <td align="right">7.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.75</td>
    <td align="right">22.97</td>
    <td align="right">19.09</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.46</td>
    <td align="right">6.56</td>
    <td align="right">6.65</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.28</td>
    <td align="right">9.56</td>
    <td align="right">9.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">52.06</td>
    <td align="right">44.90</td>
    <td align="right">20.31</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.18</td>
    <td align="right">8.99</td>
    <td align="right">9.32</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.09</td>
    <td align="right">11.60</td>
    <td align="right">13.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">73.34</td>
    <td align="right">83.17</td>
    <td align="right">24.32</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.68</td>
    <td align="right">17.47</td>
    <td align="right">17.90</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">23.88</td>
    <td align="right">16.44</td>
    <td align="right">14.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4515</td>
    <td align="right">10.28</td>
    <td align="right">9.30</td>
    <td align="right">9.30</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">12.17</td>
    <td align="right">9.52</td>
    <td align="right">9.62</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.82</td>
    <td align="right">4.19</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.36</td>
    <td align="right">14.73</td>
    <td align="right">13.95</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.97</td>
    <td align="right">14.03</td>
    <td align="right">14.29</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.62</td>
    <td align="right">5.49</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">29.21</td>
    <td align="right">21.55</td>
    <td align="right">24.04</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">29.39</td>
    <td align="right">27.06</td>
    <td align="right">26.87</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.31</td>
    <td align="right">13.05</td>
    <td align="right">10.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">34.59</td>
    <td align="right">30.93</td>
    <td align="right">29.83</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">40.28</td>
    <td align="right">29.81</td>
    <td align="right">30.68</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.47</td>
    <td align="right">12.47</td>
    <td align="right">10.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4625</td>
    <td align="right">3.73</td>
    <td align="right">4.07</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.10</td>
    <td align="right">5.93</td>
    <td align="right">5.92</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.20</td>
    <td align="right">5.88</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">4.47</td>
    <td align="right">6.38</td>
    <td align="right">5.50</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">6.22</td>
    <td align="right">7.48</td>
    <td align="right">6.36</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.50</td>
    <td align="right">7.66</td>
    <td align="right">6.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.83</td>
    <td align="right">10.21</td>
    <td align="right">7.84</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.62</td>
    <td align="right">12.10</td>
    <td align="right">10.06</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">12.50</td>
    <td align="right">12.62</td>
    <td align="right">10.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">12.98</td>
    <td align="right">14.65</td>
    <td align="right">10.87</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">16.66</td>
    <td align="right">17.97</td>
    <td align="right">13.51</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">16.75</td>
    <td align="right">18.16</td>
    <td align="right">13.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">10.36</td>
    <td align="right">9.70</td>
    <td align="right">14.03</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">10.58</td>
    <td align="right">9.72</td>
    <td align="right">14.07</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.14</td>
    <td align="right">13.01</td>
    <td align="right">17.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">14.26</td>
    <td align="right">12.66</td>
    <td align="right">13.39</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">14.54</td>
    <td align="right">12.42</td>
    <td align="right">13.89</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">17.18</td>
    <td align="right">15.82</td>
    <td align="right">15.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">19.62</td>
    <td align="right">18.88</td>
    <td align="right">15.19</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">19.92</td>
    <td align="right">18.90</td>
    <td align="right">14.65</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">30.46</td>
    <td align="right">26.94</td>
    <td align="right">22.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">40.25</td>
    <td align="right">40.23</td>
    <td align="right">21.31</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">41.70</td>
    <td align="right">39.43</td>
    <td align="right">17.57</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">35.89</td>
    <td align="right">32.47</td>
    <td align="right">18.96</td>
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
    <td align="right">60.68</td>
    <td align="right">29.88</td>
    <td align="right">14.01</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">27.37</td>
    <td align="right">41.76</td>
    <td align="right">36.08</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.50</td>
    <td align="right">15.51</td>
    <td align="right">15.51</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.09</td>
    <td align="right">19.13</td>
    <td align="right">19.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.89</td>
    <td align="right">63.42</td>
    <td align="right">38.89</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.27</td>
    <td align="right">19.54</td>
    <td align="right">19.60</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.08</td>
    <td align="right">18.59</td>
    <td align="right">18.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.94</td>
    <td align="right">78.46</td>
    <td align="right">38.43</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.36</td>
    <td align="right">18.42</td>
    <td align="right">18.54</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.98</td>
    <td align="right">18.22</td>
    <td align="right">18.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">53.00</td>
    <td align="right">89.56</td>
    <td align="right">34.76</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">17.31</td>
    <td align="right">18.51</td>
    <td align="right">18.53</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.10</td>
    <td align="right">19.52</td>
    <td align="right">19.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4144</td>
    <td align="right">16.21</td>
    <td align="right">21.24</td>
    <td align="right">21.22</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.62</td>
    <td align="right">22.15</td>
    <td align="right">22.18</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.90</td>
    <td align="right">13.53</td>
    <td align="right">13.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.26</td>
    <td align="right">25.92</td>
    <td align="right">25.96</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.58</td>
    <td align="right">27.60</td>
    <td align="right">27.67</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.01</td>
    <td align="right">16.28</td>
    <td align="right">15.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.88</td>
    <td align="right">32.97</td>
    <td align="right">32.93</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.59</td>
    <td align="right">46.43</td>
    <td align="right">46.77</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.90</td>
    <td align="right">19.47</td>
    <td align="right">19.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">32.88</td>
    <td align="right">33.74</td>
    <td align="right">33.78</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">75.84</td>
    <td align="right">55.00</td>
    <td align="right">54.98</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">21.91</td>
    <td align="right">23.79</td>
    <td align="right">23.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4627</td>
    <td align="right">15.28</td>
    <td align="right">15.51</td>
    <td align="right">15.51</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.11</td>
    <td align="right">21.24</td>
    <td align="right">21.24</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.65</td>
    <td align="right">22.18</td>
    <td align="right">22.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.78</td>
    <td align="right">20.42</td>
    <td align="right">20.44</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.26</td>
    <td align="right">25.96</td>
    <td align="right">25.94</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.62</td>
    <td align="right">27.64</td>
    <td align="right">27.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.26</td>
    <td align="right">24.75</td>
    <td align="right">24.76</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.88</td>
    <td align="right">32.91</td>
    <td align="right">32.94</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.57</td>
    <td align="right">46.46</td>
    <td align="right">46.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">33.30</td>
    <td align="right">35.12</td>
    <td align="right">35.06</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">32.86</td>
    <td align="right">33.76</td>
    <td align="right">33.79</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">75.90</td>
    <td align="right">55.02</td>
    <td align="right">55.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">12.80</td>
    <td align="right">15.94</td>
    <td align="right">23.58</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.09</td>
    <td align="right">20.71</td>
    <td align="right">25.36</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.33</td>
    <td align="right">29.17</td>
    <td align="right">34.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.56</td>
    <td align="right">23.25</td>
    <td align="right">24.69</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.34</td>
    <td align="right">28.11</td>
    <td align="right">26.18</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.47</td>
    <td align="right">33.14</td>
    <td align="right">30.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.37</td>
    <td align="right">25.97</td>
    <td align="right">24.25</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.56</td>
    <td align="right">33.43</td>
    <td align="right">25.77</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">46.95</td>
    <td align="right">41.66</td>
    <td align="right">33.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">26.59</td>
    <td align="right">26.51</td>
    <td align="right">24.57</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">36.03</td>
    <td align="right">38.00</td>
    <td align="right">26.16</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">46.36</td>
    <td align="right">41.87</td>
    <td align="right">30.36</td>
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
    <td align="right">67.98</td>
    <td align="right">96.11</td>
    <td align="right">17.42</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">27.50</td>
    <td align="right">42.31</td>
    <td align="right">38.71</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.75</td>
    <td align="right">15.52</td>
    <td align="right">15.51</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.39</td>
    <td align="right">19.20</td>
    <td align="right">19.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.17</td>
    <td align="right">61.66</td>
    <td align="right">40.09</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.26</td>
    <td align="right">19.83</td>
    <td align="right">19.84</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.13</td>
    <td align="right">18.70</td>
    <td align="right">18.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">42.80</td>
    <td align="right">73.88</td>
    <td align="right">38.33</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.03</td>
    <td align="right">18.42</td>
    <td align="right">18.58</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">17.80</td>
    <td align="right">18.23</td>
    <td align="right">18.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">55.25</td>
    <td align="right">93.28</td>
    <td align="right">37.53</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">18.53</td>
    <td align="right">19.40</td>
    <td align="right">19.36</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">19.62</td>
    <td align="right">20.58</td>
    <td align="right">20.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4525</td>
    <td align="right">16.39</td>
    <td align="right">21.63</td>
    <td align="right">21.78</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.79</td>
    <td align="right">22.80</td>
    <td align="right">22.91</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.06</td>
    <td align="right">13.81</td>
    <td align="right">13.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.03</td>
    <td align="right">25.60</td>
    <td align="right">25.43</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">45.30</td>
    <td align="right">28.16</td>
    <td align="right">27.98</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.96</td>
    <td align="right">16.48</td>
    <td align="right">15.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.25</td>
    <td align="right">41.21</td>
    <td align="right">42.83</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">70.52</td>
    <td align="right">49.39</td>
    <td align="right">50.18</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.41</td>
    <td align="right">18.62</td>
    <td align="right">18.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">34.68</td>
    <td align="right">36.75</td>
    <td align="right">37.33</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">109.51</td>
    <td align="right">72.47</td>
    <td align="right">63.77</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">50.58</td>
    <td align="right">33.34</td>
    <td align="right">27.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4723</td>
    <td align="right">15.68</td>
    <td align="right">16.34</td>
    <td align="right">15.98</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.53</td>
    <td align="right">21.52</td>
    <td align="right">21.59</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.32</td>
    <td align="right">23.79</td>
    <td align="right">23.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.59</td>
    <td align="right">20.07</td>
    <td align="right">20.05</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.02</td>
    <td align="right">25.49</td>
    <td align="right">25.38</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">48.47</td>
    <td align="right">35.25</td>
    <td align="right">31.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">34.54</td>
    <td align="right">24.40</td>
    <td align="right">26.78</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.66</td>
    <td align="right">53.11</td>
    <td align="right">50.62</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.65</td>
    <td align="right">50.72</td>
    <td align="right">49.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">70.97</td>
    <td align="right">60.45</td>
    <td align="right">39.79</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">34.83</td>
    <td align="right">36.61</td>
    <td align="right">36.82</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">79.62</td>
    <td align="right">58.23</td>
    <td align="right">57.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">12.89</td>
    <td align="right">16.39</td>
    <td align="right">24.64</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.35</td>
    <td align="right">21.08</td>
    <td align="right">25.82</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">32.79</td>
    <td align="right">30.42</td>
    <td align="right">36.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">20.78</td>
    <td align="right">22.99</td>
    <td align="right">25.04</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">28.81</td>
    <td align="right">28.31</td>
    <td align="right">26.43</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">43.02</td>
    <td align="right">47.62</td>
    <td align="right">33.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.93</td>
    <td align="right">30.43</td>
    <td align="right">24.84</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">33.19</td>
    <td align="right">40.76</td>
    <td align="right">36.48</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">50.32</td>
    <td align="right">45.55</td>
    <td align="right">38.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">30.31</td>
    <td align="right">31.55</td>
    <td align="right">37.53</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">62.88</td>
    <td align="right">41.02</td>
    <td align="right">27.72</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">65.52</td>
    <td align="right">57.56</td>
    <td align="right">58.37</td>
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
    <td align="right">62.04</td>
    <td align="right">10.70</td>
    <td align="right">7.81</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">13.77</td>
    <td align="right">22.65</td>
    <td align="right">26.51</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">10.39</td>
    <td align="right">12.44</td>
    <td align="right">12.42</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.78</td>
    <td align="right">13.86</td>
    <td align="right">13.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.36</td>
    <td align="right">35.00</td>
    <td align="right">29.28</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">31.31</td>
    <td align="right">14.19</td>
    <td align="right">14.16</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">14.80</td>
    <td align="right">15.44</td>
    <td align="right">15.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.98</td>
    <td align="right">47.27</td>
    <td align="right">29.55</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.90</td>
    <td align="right">15.45</td>
    <td align="right">15.46</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">16.40</td>
    <td align="right">16.81</td>
    <td align="right">16.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.40</td>
    <td align="right">60.42</td>
    <td align="right">31.21</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">16.30</td>
    <td align="right">16.35</td>
    <td align="right">16.34</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">17.30</td>
    <td align="right">17.91</td>
    <td align="right">17.91</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4144</td>
    <td align="right">12.73</td>
    <td align="right">16.16</td>
    <td align="right">16.14</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.28</td>
    <td align="right">16.76</td>
    <td align="right">16.79</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.04</td>
    <td align="right">9.39</td>
    <td align="right">9.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.38</td>
    <td align="right">22.53</td>
    <td align="right">22.58</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.81</td>
    <td align="right">22.45</td>
    <td align="right">22.40</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.28</td>
    <td align="right">14.18</td>
    <td align="right">14.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.20</td>
    <td align="right">32.18</td>
    <td align="right">32.21</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.69</td>
    <td align="right">30.92</td>
    <td align="right">30.87</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.65</td>
    <td align="right">17.52</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.93</td>
    <td align="right">35.88</td>
    <td align="right">35.85</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.16</td>
    <td align="right">35.88</td>
    <td align="right">35.89</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.39</td>
    <td align="right">20.49</td>
    <td align="right">20.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4627</td>
    <td align="right">6.58</td>
    <td align="right">9.39</td>
    <td align="right">9.40</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.68</td>
    <td align="right">16.13</td>
    <td align="right">16.09</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.31</td>
    <td align="right">16.76</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.20</td>
    <td align="right">13.74</td>
    <td align="right">13.69</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.39</td>
    <td align="right">22.57</td>
    <td align="right">22.56</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.82</td>
    <td align="right">22.45</td>
    <td align="right">22.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.12</td>
    <td align="right">17.66</td>
    <td align="right">17.69</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.12</td>
    <td align="right">32.21</td>
    <td align="right">32.16</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.70</td>
    <td align="right">30.88</td>
    <td align="right">30.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.07</td>
    <td align="right">21.00</td>
    <td align="right">20.86</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.03</td>
    <td align="right">35.80</td>
    <td align="right">35.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.03</td>
    <td align="right">35.92</td>
    <td align="right">35.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">10.24</td>
    <td align="right">10.82</td>
    <td align="right">18.84</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.31</td>
    <td align="right">16.30</td>
    <td align="right">20.04</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.92</td>
    <td align="right">34.31</td>
    <td align="right">36.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">14.99</td>
    <td align="right">16.31</td>
    <td align="right">19.22</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.80</td>
    <td align="right">23.50</td>
    <td align="right">20.69</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">53.67</td>
    <td align="right">37.67</td>
    <td align="right">36.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">17.95</td>
    <td align="right">18.94</td>
    <td align="right">18.62</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.06</td>
    <td align="right">30.03</td>
    <td align="right">20.48</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.75</td>
    <td align="right">45.91</td>
    <td align="right">38.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">20.19</td>
    <td align="right">21.26</td>
    <td align="right">19.88</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">30.08</td>
    <td align="right">35.70</td>
    <td align="right">21.47</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">64.42</td>
    <td align="right">47.97</td>
    <td align="right">37.70</td>
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
    <td align="right">77.37</td>
    <td align="right">46.89</td>
    <td align="right">10.57</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">14.46</td>
    <td align="right">23.37</td>
    <td align="right">28.83</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">10.74</td>
    <td align="right">12.82</td>
    <td align="right">12.83</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">29.88</td>
    <td align="right">14.25</td>
    <td align="right">14.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.51</td>
    <td align="right">34.86</td>
    <td align="right">30.02</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">31.41</td>
    <td align="right">13.99</td>
    <td align="right">13.95</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">14.58</td>
    <td align="right">15.11</td>
    <td align="right">15.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.71</td>
    <td align="right">47.60</td>
    <td align="right">29.81</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">14.63</td>
    <td align="right">15.16</td>
    <td align="right">15.15</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">16.15</td>
    <td align="right">16.47</td>
    <td align="right">16.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">33.00</td>
    <td align="right">63.94</td>
    <td align="right">32.03</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">16.91</td>
    <td align="right">16.78</td>
    <td align="right">17.23</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">19.48</td>
    <td align="right">19.38</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4525</td>
    <td align="right">13.01</td>
    <td align="right">17.05</td>
    <td align="right">17.07</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.61</td>
    <td align="right">18.07</td>
    <td align="right">18.06</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.35</td>
    <td align="right">9.73</td>
    <td align="right">9.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.03</td>
    <td align="right">22.08</td>
    <td align="right">22.28</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">20.17</td>
    <td align="right">24.94</td>
    <td align="right">22.43</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.42</td>
    <td align="right">14.34</td>
    <td align="right">14.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.31</td>
    <td align="right">33.33</td>
    <td align="right">33.53</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.98</td>
    <td align="right">31.60</td>
    <td align="right">31.49</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.37</td>
    <td align="right">16.89</td>
    <td align="right">16.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">29.02</td>
    <td align="right">38.70</td>
    <td align="right">38.93</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">34.18</td>
    <td align="right">36.68</td>
    <td align="right">36.61</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">17.28</td>
    <td align="right">21.37</td>
    <td align="right">22.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4723</td>
    <td align="right">6.86</td>
    <td align="right">9.83</td>
    <td align="right">9.84</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.94</td>
    <td align="right">17.02</td>
    <td align="right">17.04</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.60</td>
    <td align="right">18.07</td>
    <td align="right">18.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.93</td>
    <td align="right">13.43</td>
    <td align="right">13.41</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.02</td>
    <td align="right">22.06</td>
    <td align="right">22.18</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.01</td>
    <td align="right">22.07</td>
    <td align="right">22.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">12.87</td>
    <td align="right">17.04</td>
    <td align="right">17.06</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.98</td>
    <td align="right">33.01</td>
    <td align="right">33.03</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.85</td>
    <td align="right">31.42</td>
    <td align="right">31.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">17.11</td>
    <td align="right">22.19</td>
    <td align="right">22.14</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">27.76</td>
    <td align="right">37.87</td>
    <td align="right">37.77</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">34.24</td>
    <td align="right">36.56</td>
    <td align="right">36.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">11.83</td>
    <td align="right">11.15</td>
    <td align="right">19.17</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">13.63</td>
    <td align="right">16.96</td>
    <td align="right">20.63</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.67</td>
    <td align="right">33.71</td>
    <td align="right">37.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">14.85</td>
    <td align="right">16.09</td>
    <td align="right">19.18</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">20.03</td>
    <td align="right">23.37</td>
    <td align="right">20.74</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">53.86</td>
    <td align="right">37.10</td>
    <td align="right">36.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">18.00</td>
    <td align="right">18.93</td>
    <td align="right">18.64</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">23.77</td>
    <td align="right">30.12</td>
    <td align="right">20.49</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">60.60</td>
    <td align="right">42.75</td>
    <td align="right">35.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">21.17</td>
    <td align="right">22.69</td>
    <td align="right">20.14</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">31.46</td>
    <td align="right">37.69</td>
    <td align="right">22.22</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">71.27</td>
    <td align="right">51.72</td>
    <td align="right">39.67</td>
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
    <td align="right">42.65</td>
    <td align="right">8.55</td>
    <td align="right">6.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">59.65</td>
    <td align="right">57.26</td>
    <td align="right">42.34</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">22.74</td>
    <td align="right">22.78</td>
    <td align="right">26.57</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">24.77</td>
    <td align="right">25.88</td>
    <td align="right">29.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">88.01</td>
    <td align="right">83.00</td>
    <td align="right">44.38</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">25.85</td>
    <td align="right">23.96</td>
    <td align="right">26.22</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.94</td>
    <td align="right">29.22</td>
    <td align="right">29.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">108.62</td>
    <td align="right">101.69</td>
    <td align="right">43.69</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">28.09</td>
    <td align="right">25.50</td>
    <td align="right">26.79</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.82</td>
    <td align="right">31.08</td>
    <td align="right">31.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">136.88</td>
    <td align="right">126.98</td>
    <td align="right">44.37</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">30.58</td>
    <td align="right">27.01</td>
    <td align="right">27.87</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">32.81</td>
    <td align="right">33.14</td>
    <td align="right">33.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4144</td>
    <td align="right">24.14</td>
    <td align="right">45.85</td>
    <td align="right">44.48</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.65</td>
    <td align="right">46.35</td>
    <td align="right">45.08</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.60</td>
    <td align="right">25.02</td>
    <td align="right">24.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">31.08</td>
    <td align="right">62.05</td>
    <td align="right">61.63</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.30</td>
    <td align="right">66.17</td>
    <td align="right">63.48</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.78</td>
    <td align="right">36.09</td>
    <td align="right">25.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">42.04</td>
    <td align="right">84.67</td>
    <td align="right">85.10</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">47.62</td>
    <td align="right">82.42</td>
    <td align="right">83.64</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.81</td>
    <td align="right">54.72</td>
    <td align="right">39.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">46.49</td>
    <td align="right">95.83</td>
    <td align="right">95.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">53.93</td>
    <td align="right">100.22</td>
    <td align="right">100.64</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.11</td>
    <td align="right">55.53</td>
    <td align="right">39.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4823</td>
    <td align="right">18.68</td>
    <td align="right">26.06</td>
    <td align="right">26.16</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.69</td>
    <td align="right">29.00</td>
    <td align="right">29.05</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.94</td>
    <td align="right">30.88</td>
    <td align="right">30.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.97</td>
    <td align="right">46.32</td>
    <td align="right">35.05</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.63</td>
    <td align="right">39.70</td>
    <td align="right">27.62</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">20.99</td>
    <td align="right">51.70</td>
    <td align="right">40.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.62</td>
    <td align="right">54.19</td>
    <td align="right">38.44</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.11</td>
    <td align="right">52.78</td>
    <td align="right">34.91</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.23</td>
    <td align="right">61.00</td>
    <td align="right">43.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.70</td>
    <td align="right">55.10</td>
    <td align="right">39.15</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.54</td>
    <td align="right">65.09</td>
    <td align="right">44.48</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.45</td>
    <td align="right">64.02</td>
    <td align="right">44.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">23.75</td>
    <td align="right">22.38</td>
    <td align="right">29.65</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.88</td>
    <td align="right">42.91</td>
    <td align="right">35.04</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">33.66</td>
    <td align="right">53.30</td>
    <td align="right">40.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">33.39</td>
    <td align="right">32.94</td>
    <td align="right">30.15</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">36.43</td>
    <td align="right">60.27</td>
    <td align="right">35.60</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.69</td>
    <td align="right">60.52</td>
    <td align="right">37.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">39.34</td>
    <td align="right">36.84</td>
    <td align="right">30.77</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">42.13</td>
    <td align="right">73.50</td>
    <td align="right">35.43</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">50.94</td>
    <td align="right">78.73</td>
    <td align="right">40.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">48.55</td>
    <td align="right">48.45</td>
    <td align="right">32.05</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">54.56</td>
    <td align="right">95.19</td>
    <td align="right">37.69</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">61.58</td>
    <td align="right">98.96</td>
    <td align="right">40.55</td>
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
    <td align="right">71.25</td>
    <td align="right">38.11</td>
    <td align="right">19.46</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">72.82</td>
    <td align="right">69.12</td>
    <td align="right">48.36</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">43.45</td>
    <td align="right">29.00</td>
    <td align="right">34.67</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">33.28</td>
    <td align="right">30.00</td>
    <td align="right">38.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">177.17</td>
    <td align="right">175.27</td>
    <td align="right">81.32</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">83.99</td>
    <td align="right">57.71</td>
    <td align="right">60.70</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">67.70</td>
    <td align="right">93.46</td>
    <td align="right">72.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">204.59</td>
    <td align="right">248.95</td>
    <td align="right">77.59</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">58.01</td>
    <td align="right">51.95</td>
    <td align="right">38.79</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">53.12</td>
    <td align="right">54.13</td>
    <td align="right">56.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">289.72</td>
    <td align="right">246.30</td>
    <td align="right">64.24</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">71.18</td>
    <td align="right">49.33</td>
    <td align="right">47.07</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">73.23</td>
    <td align="right">88.15</td>
    <td align="right">90.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4525</td>
    <td align="right">34.49</td>
    <td align="right">56.21</td>
    <td align="right">62.37</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">39.59</td>
    <td align="right">48.70</td>
    <td align="right">48.23</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.91</td>
    <td align="right">29.29</td>
    <td align="right">29.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">38.46</td>
    <td align="right">89.58</td>
    <td align="right">86.70</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">87.26</td>
    <td align="right">116.30</td>
    <td align="right">122.03</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">23.96</td>
    <td align="right">94.92</td>
    <td align="right">85.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">108.53</td>
    <td align="right">128.63</td>
    <td align="right">119.08</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">80.53</td>
    <td align="right">133.64</td>
    <td align="right">135.24</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">89.61</td>
    <td align="right">122.95</td>
    <td align="right">100.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">95.08</td>
    <td align="right">115.46</td>
    <td align="right">110.10</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">97.49</td>
    <td align="right">137.70</td>
    <td align="right">140.26</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">92.45</td>
    <td align="right">138.92</td>
    <td align="right">124.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4632</td>
    <td align="right">37.12</td>
    <td align="right">71.89</td>
    <td align="right">90.65</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">56.52</td>
    <td align="right">94.48</td>
    <td align="right">86.36</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">47.46</td>
    <td align="right">88.27</td>
    <td align="right">101.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">61.00</td>
    <td align="right">132.04</td>
    <td align="right">121.56</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">37.27</td>
    <td align="right">114.71</td>
    <td align="right">99.92</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">64.24</td>
    <td align="right">110.72</td>
    <td align="right">96.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">90.36</td>
    <td align="right">135.38</td>
    <td align="right">128.60</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">98.13</td>
    <td align="right">136.22</td>
    <td align="right">105.84</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">101.27</td>
    <td align="right">120.91</td>
    <td align="right">77.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">85.77</td>
    <td align="right">123.55</td>
    <td align="right">116.07</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">77.06</td>
    <td align="right">133.44</td>
    <td align="right">116.21</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">68.15</td>
    <td align="right">128.23</td>
    <td align="right">120.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">43.77</td>
    <td align="right">40.15</td>
    <td align="right">42.32</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">31.38</td>
    <td align="right">56.68</td>
    <td align="right">55.92</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">76.23</td>
    <td align="right">106.40</td>
    <td align="right">70.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">74.34</td>
    <td align="right">79.29</td>
    <td align="right">55.43</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">67.47</td>
    <td align="right">98.56</td>
    <td align="right">60.27</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">103.14</td>
    <td align="right">93.76</td>
    <td align="right">62.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">98.81</td>
    <td align="right">97.02</td>
    <td align="right">57.85</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">97.50</td>
    <td align="right">123.65</td>
    <td align="right">69.13</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">130.35</td>
    <td align="right">151.25</td>
    <td align="right">85.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">114.76</td>
    <td align="right">104.26</td>
    <td align="right">59.75</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">103.89</td>
    <td align="right">145.59</td>
    <td align="right">68.29</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">137.43</td>
    <td align="right">154.90</td>
    <td align="right">80.51</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
